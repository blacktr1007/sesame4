from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

from pysesame3.chsesame2 import CHSesame2
from pysesame3.const import CHSesame2ShadowStatus


@dataclass
class OpenSesame:
    device: CHSesame2
    history_tag: str

    def _current_date(self) -> str:
        return datetime.now(tz=ZoneInfo("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")

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
