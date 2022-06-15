import yaml
from dacite.core import from_dict
from pysesame3.auth import WebAPIAuth
from pysesame3.chsesame2 import CHSesame2

from config.config import ConfigSchema
from open_sesame.core import OpenSesame


def create_oepn_sesame() -> OpenSesame:
    config_file = "/etc/secrets/config.yml"
    with open(config_file, "r") as config_fp:
        config = from_dict(data_class=ConfigSchema, data=yaml.safe_load(config_fp))

    auth = WebAPIAuth(apikey=config.sesame.api_key)
    device = CHSesame2(
        authenticator=auth,
        device_uuid=str(config.sesame.device_uuid),
        secret_key=config.sesame.secret_key,
    )

    return OpenSesame(device=device, history_tag=config.history_tag)


def lock():
    sesame = create_oepn_sesame()
    sesame.lock()


def unlock():
    sesame = create_oepn_sesame()
    sesame.unlock()
