from math import log2


class _SizeProc:
    def __init__(self, val: float) -> None:
        self.__bytes: float = val

    def __repr__(self) -> str:
        # ! May need to use `round` function
        tempsize: int = 0 if (self.__bytes == 0) else (int)(log2(self.__bytes) / 10)

        match tempsize:
            case 0:
                return f"{round(self.bytes, 1):<7}B"
            case 1:
                return f"{round(self.kb, 1):<7}KB"
            case 2:
                return f"{round(self.mb, 1):<7}MB"
            case _:
                return f"{round(self.gb, 1):<7}GB"

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, _SizeProc) and self.__bytes == __value.__bytes

    @property
    def bytes(self) -> float:
        return self.__bytes

    @property
    def kb(self) -> float:
        return self.bytes / 1024

    @property
    def mb(self) -> float:
        return self.kb / 1024

    @property
    def gb(self) -> float:
        return self.mb / 1024


class _TimeProc:
    def __init__(self, sec: float) -> None:
        self.__sec: float = sec

    def __repr__(self) -> str:
        if self.hrs > 24:
            return f"{round(self.days, 2):<6}days"

        elif self.min > 59:
            return f"{round(self.hrs, 2):<6}hrs"

        elif self.sec > 59:
            return f"{round(self.min, 2):<6}min"

        return f"{round(self.sec, 2):<6}sec"

    def __eq__(self, val: object) -> bool:
        return isinstance(val, _TimeProc) and self.__sec == val.__sec

    @property
    def sec(self) -> float:
        return self.__sec

    @property
    def min(self) -> float:
        return self.sec / 60

    @property
    def hrs(self) -> float:
        return self.min / 60

    @property
    def days(self) -> float:
        return self.hrs / 24


class _StatusProc:
    def __init__(self, running: bool) -> None:
        self.running: bool = running

    def __repr__(self) -> str:
        if self.running:
            return "[bold green]Running[/bold green]"
        return "[bold red]IDLE[/bold red]"
