from dataclasses import dataclass, field
from datetime import datetime

import pytz
from pysesame3.chsesame2 import CHSesame2
from pysesame3.const import CHSesame2ShadowStatus
from pytz.tzinfo import DstTzInfo, StaticTzInfo


@dataclass
class OpenSesame:
    device: CHSesame2
    history_tag: str
    location: StaticTzInfo | DstTzInfo | pytz.UTC.__class__ = field(init=False)

    def __post_init__(self):
        self.location = pytz.timezone("Asia/Tokyo")

    def _current_date(self) -> str:
        return self.location.localize(datetime.now()).strftime("%Y/%m/%d %H:%M:%S")

    def lock(self) -> str:
        if self.device.getDeviceShadowStatus() == CHSesame2ShadowStatus.LockedWm:
            return "Device is already Locked!"
        self.device.lock(history_tag=self.history_tag)
        return f"Locked at {self._current_date()}"

    def unlock(self) -> str:
        if self.device.getDeviceShadowStatus() == CHSesame2ShadowStatus.UnlockedWm:
            return "Device is already Unlocked!"
        self.device.unlock(history_tag=self.history_tag)
        return f"Unlocked at {self._current_date()}"
