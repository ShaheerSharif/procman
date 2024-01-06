import psutil

from .process import Proc

from psutil import Process
from typing import Iterator, List
from rich.traceback import install


install()


def sort_proc_list(
    proc_iter: Iterator[Process], sort_key, descending: bool = True
) -> List[Process]:
    return sorted(proc_iter)


def __get_valid_process(process: Process) -> Process:
    try:
        return process
    except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
        return None


def __conv_processes_to_procs(processes: List[Process]) -> Proc:
    return [Proc(process) for process in processes if process is not None]


def generate_proc_list(size: int, sortby, descending: bool = True) -> List[Proc]:
    """
    The function `generate_proc_list` takes in a size parameter and returns a list of processes sorted
    by name, with an optional sorting function and sorting order.

    Arguments:

    * `size`: The `size` parameter specifies the number of processes to include in the list.
    * `sortby`: The `sortby` parameter is a function that determines how the process list should be
    sorted. It takes a list of `Proc` objects and returns a sorted list based on a specific criteria. By
    default, the `sortby_mem_usage` function is used, which sorts the processes by their memory consumption.
    * `descending`: Determines whether list should be in descending or ascending order(Default).

    Returns:

    The function `generate_proc_list` returns a list of `Proc` objects.
    """
    proc_list: List[Process] = [
        process
        for process in psutil.process_iter()
        if __get_valid_process(process) is not None
    ]

    return __conv_processes_to_procs(sortby(proc_list, descending)[:size])
