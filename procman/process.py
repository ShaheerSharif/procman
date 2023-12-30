from time import time
from psutil import Process

from .units import SizeProc, TimeProc


class Proc:
    def __init__(self, process: Process) -> None:
        self._process: Process = process
        self._start: float = process.create_time()
        self._cpu_perc: float = 0

    def __eq__(self, other):
        return isinstance(other, Proc) and other.pid == self.pid

    @property
    def name(self) -> str:
        return self._process.name()

    @property
    def username(self) -> str:
        return self._process.username()

    @property
    def active(self) -> bool:
        return self._process.is_running()

    @property
    def pid(self) -> int:
        return self._process.pid

    @property
    def ppid(self) -> int:
        return self._process.ppid()

    def uptime(self) -> TimeProc:
        if self.active:
            return TimeProc(time() - self._start)
        return TimeProc(0)

    def get_mem_perc(self) -> float:
        return Process(self.pid).memory_percent("vms") if (self.active) else 0

    def get_mem_usage(self) -> SizeProc:
        if self.active:
            return SizeProc(self._process.memory_info()[0])  # Get size in bytes
        return SizeProc(0)

    def kill(self) -> None:
        self._start = 0
        self._process.kill()
