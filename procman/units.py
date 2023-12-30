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
                return f"{round(self.kb, 1)}KB"
            case 2:
                return f"{round(self.mb, 1)}MB"
            case _:
                return f"{round(self.gb, 1)}GB"

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, SizeProc) and self._bytes == __value._bytes

    @property
    def bytes(self) -> float:
        return self._bytes

    @property
    def kb(self) -> float:
        return self.bytes / 1024

    @property
    def mb(self) -> float:
        return self.kb / 1024

    @property
    def gb(self) -> float:
        return self.mb / 1024


class TimeProc:
    def __init__(self, val: timedelta) -> None:
        self._time: timedelta = val

    def __repr__(self) -> str:
        if self.min > 59:
            return f"{round(self.hrs, 2)}hr"

        elif self.sec > 59:
            return f"{round(self.min, 2)}m"

        return f"{round(self.sec, 2)}s"

    def __eq__(self, __value: object) -> bool:
        return (
            isinstance(__value, TimeProc)
            and self._time.total_seconds() == __value._time.total_seconds()
        )

    @property
    def sec(self) -> float:
        return self._time.total_seconds()

    @property
    def min(self) -> float:
        return self.sec / 60

    @property
    def hrs(self) -> float:
        return self.min / 60
