from dataclasses import dataclass

from pysesame3.chsesame2 import CHSesame2


@dataclass
class OpenSesame:
    device: CHSesame2
    history_tag: str

    def lock(self):
        self.device.lock(history_tag=self.history_tag)

    def unlock(self):
        self.device.unlock(history_tag=self.history_tag)
