from typing import cast

import yaml
from dacite.core import from_dict
from flask.wrappers import Request
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


def main(request: Request):
    config_file = "/etc/secrets/config.yml"
    with open(config_file, "r") as config_fp:
        config = from_dict(data_class=ConfigSchema, data=yaml.safe_load(config_fp))

    try:
        verify_slack_signature(request=request, signing_secret=config.slack.signing_secret)
    except ValueError as e:
        return str(e)

    auth = WebAPIAuth(apikey=config.sesame.api_key)
    device = CHSesame2(
        authenticator=auth,
        device_uuid=str(config.sesame.device_uuid),
        secret_key=config.sesame.secret_key,
    )

    sesame: OpenSesame = OpenSesame(device=device, history_tag=config.history_tag)

    if request.method == "POST":
        action: str = request.args.get("action", "")
    elif request.method == "GET":
        action: str = cast(dict[str, str], request.get_json())["client_id"] if request.is_json else ""
    else:
        return False

    if action in ["unlock", "sesame_unlock"]:
        return sesame.unlock()
    else:
        return sesame.lock()
