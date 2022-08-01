import json
from base64 import b64decode
from typing import Any, cast

import yaml
from dacite.core import from_dict
from flask.wrappers import Request
from google.cloud.pubsub_v1 import PublisherClient
from google.cloud.pubsub_v1.futures import Future
from pysesame3.auth import WebAPIAuth
from pysesame3.chsesame2 import CHSesame2
from slack_sdk.signature import SignatureVerifier

from config.config import ConfigSchema
from open_sesame.core import OpenSesame


def verify_slack_signature(request: Request, signing_secret: str):
    request.get_data()  # Decodes received requests into request.data

    verifier = SignatureVerifier(signing_secret)

    if not verifier.is_valid_request(request.data, request.headers):
        raise ValueError("Invalid request/credentials.")


def subscribe(event: dict[str, Any], context: Any):
    config_file = "/etc/secrets/config.yml"
    with open(config_file, "r") as config_fp:
        config = from_dict(data_class=ConfigSchema, data=yaml.safe_load(config_fp))

    auth = WebAPIAuth(apikey=config.sesame.api_key)
    device = CHSesame2(
        authenticator=auth,
        device_uuid=str(config.sesame.device_uuid),
        secret_key=config.sesame.secret_key,
    )

    sesame: OpenSesame = OpenSesame(device=device, history_tag=config.history_tag)

    action: str = json.loads(b64decode(event["data"]).decode())["action"]
    if action in ["unlock", "sesame_unlock"]:
        sesame.unlock()
    else:
        sesame.lock()


def publish(request: Request):
    if request.method != "POST":
        return "Only POST requests are accepted", 405

    config_file = "/etc/secrets/config.yml"
    with open(config_file, "r") as config_fp:
        config = from_dict(data_class=ConfigSchema, data=yaml.safe_load(config_fp))

    try:
        verify_slack_signature(request=request, signing_secret=config.slack.signing_secret)
    except ValueError as e:
        return str(e)

    publisher = PublisherClient()
    action: str
    if not (action := request.args.get("action", "")):
        action = cast(dict[str, str], request.get_json())["client_id"] if request.is_json else ""
    message = json.dumps({"action": action})

    try:
        publish_future: Future = publisher.publish(
            publisher.topic_path(config.gcp.project_id, config.gcp.topic),
            data=message.encode("utf-8"),
        )
        publish_future.result()
        return f"{action}: Accepted."
    except Exception as e:
        return f"{action}: {e}"
