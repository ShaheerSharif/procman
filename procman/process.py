from datetime import datetime
from threading import Thread
from psutil import Process

import psutil

from .units import SizeProc, TimeProc


class Proc:
    def __init__(self, process: Process) -> None:
        self._process: Process = process
        self._start: TimeProc = TimeProc(0)
        self._cpu_usage: float = 0
        self._thread: Thread = None
        self.name = process.name()

    def __eq__(self, other):
        """
        Checks if two Proc instances are equal based on their names.

        Parameters:
            other (Proc): Another Proc instance.

        Returns:
            bool: True if the names are equal, False otherwise.
        """
        # TODO Might need to add more
        return isinstance(other, Proc) and other.name == self.name

    @property
    def active(self) -> bool:
        return self._process.is_running()

    @property
    def pid(self) -> int:
        return self._process.pid if (self.active) else -1

    @property
    def ppid(self) -> int:
        return self._process.ppid() if (self.active) else -1

    def uptime(self) -> TimeProc:
        if self.active:
            return TimeProc(datetime.now() - self._start)
        return TimeProc(0)

    def get_mem_perc(self) -> float:
        return Process(self.pid).memory_percent("vms") if (self.active) else 0

    def get_mem_usage(self) -> SizeProc:
        if self.active:
            return SizeProc(Process(self.pid).memory_info().vms)
        return SizeProc(0)

    def update_cpu(self) -> None:
        try:
            self._cpu_usage = (
                psutil.Process(self.pid).cpu_percent(0.1) / psutil.cpu_count()
            )
        except psutil.NoSuchProcess:
            pass

    def get_cpu_perc(self) -> float:
        """
        Retrieves the CPU usage percentage.

        Returns:
            float: CPU usage percentage if active, otherwise 0.
        """
        if self.active:
            if self._thread is None or not self._thread.is_alive():
                self._thread = Thread(target=self.update_cpu)
                self._thread.setDaemon(True)
                self._thread.start()
            return self._cpu_usage
        return 0

    def kill(self) -> None:
        """
        Kills the process and resets the start time.
        """
        self._start = TimeProc(0)
        self._process.kill()
