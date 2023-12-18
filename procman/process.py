from math import log2
from datetime import timedelta


class SizeProc:
    def __init__(self, val: float) -> None:
        self._bytes: float = val

    def __repr__(self) -> str:
        # ! May need to use `round` function
        tempsize: int = 0 if (self._bytes == 0) else (int)(log2(self._bytes) / 10)

        match tempsize:
            case 0:
                return f"{round(self.bytes, 1)}B"
            case 1:
                return f"{round(self.kbytes, 1)}KB"
            case 2:
                return f"{round(self.mbytes, 1)}MB"
            case _:
                return f"{round(self.gbytes, 1)}GB"

    @property
    def bytes(self) -> float:
        return self._bytes

    @property
    def kbytes(self) -> float:
        return self.bytes / 1024

    @property
    def mbytes(self) -> float:
        return self.kbytes / 1024

    @property
    def gbytes(self) -> float:
        return self.mbytes / 1024


class TimeProc:
    def __init__(self, val: timedelta) -> None:
        self._time: timedelta = val

    def __repr__(self) -> str:
        if self.minutes > 59:
            return f"{round(self.hours, 2)}hr"

        elif self.seconds > 59:
            return f"{round(self.minutes, 2)}m"

        return f"{round(self.seconds, 2)}s"

    @property
    def seconds(self) -> float:
        return self._time.total_seconds()

    @property
    def minutes(self) -> float:
        return self.seconds / 60

    @property
    def hours(self) -> float:
        return self.minutes / 60
