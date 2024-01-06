from time import time
from psutil import Process
import psutil

from .units import _SizeProc, _TimeProc, _StatusProc


class ProcException(Exception):
    pass


class Proc:
    def __init__(self, process: Process) -> None:
        self.__process: Process = process
        self.__start: float = process.create_time()

    def __eq__(self, other):
        return isinstance(other, Proc) and other.pid == self.pid

    @property
    def name(self) -> str:
        return self.__process.name()

    @property
    def uname(self) -> str:
        return self.__process.username()

    @property
    def pid(self) -> int:
        return self.__process.pid

    @property
    def ppid(self) -> int:
        return self.__process.ppid()

    def is_running(self) -> bool:
        return self.__process.is_running()

    def status(self) -> str:
        return str(_StatusProc(self.is_running()))

    def uptime(self) -> _TimeProc:
        if self.__process.is_running():
            return _TimeProc(time() - self.__start)
        return _TimeProc(0)

    def get_mem_perc(self) -> float:
        return Process(self.pid).memory_percent("vms") if (self.is_running()) else 0

    def get_mem_usage(self) -> _SizeProc:
        if self.is_running():
            return _SizeProc(self.__process.memory_info()[0])  # Get size in bytes
        return _SizeProc(0)

    def kill(self) -> None:
        self.__start = 0
        self.__process.kill()

    def check_proc(self) -> None:
        try:
            if not self.__process.is_running():
                self.__process = None
                self.__start = 0
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            self.__process = None
            self.__start = 0
