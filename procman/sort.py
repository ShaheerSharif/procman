import psutil

from .process import Proc

from psutil import Process
from pyclbr import Function
from typing import List
from rich.traceback import install


install()


def sortby_name(proc_list: List[Proc], descending: bool) -> List[Proc]:
    """
    Arguments:

    * `proc_list`: A list of Proc objects.
    * `descending`: Determines whether list should be in descending or ascending order(Default).

    Returns:

    A sorted list of `Proc` objects, sorted by their `name` attribute.
    """
    proc_list.sort(key=lambda proc: proc.name, reverse=descending)
    return proc_list


def sortby_pid(proc_list: List[Proc], descending: bool) -> List[Proc]:
    """
    Arguments:

    * `proc_list`: A list of Proc objects.
    * `descending`: Determines whether list should be in descending or ascending order(Default).

    Returns:

    A sorted list of `Proc` objects, sorted by their `pid` attribute.
    """
    proc_list.sort(key=lambda proc: proc.pid, reverse=descending)
    return proc_list


def sortby_ppid(proc_list: List[Proc], descending: bool) -> List[Proc]:
    """
    Arguments:

    * `proc_list`: A list of Proc objects.
    * `descending`: Determines whether list should be in descending or ascending order(Default).

    Returns:

    A sorted list of `Proc` objects based on their `ppid` attribute.
    """
    proc_list.sort(key=lambda proc: proc.ppid, reverse=descending)
    return proc_list


def sortby_mem_usage(proc_list: List[Proc], descending: bool) -> List[Proc]:
    """
    Arguments:

    * `proc_list`: A list of Proc objects.
    * `descending`: Determines whether list should be in descending or ascending order(Default).

    Returns:

    A sorted list of `Proc` objects, sorted by their `memory percentage`.
    """
    proc_list.sort(key=lambda proc: proc.get_mem_usage().bytes, reverse=descending)
    return proc_list


def sortby_uptime(proc_list: List[Proc], descending: bool) -> List[Proc]:
    """
    Arguments:

    * `proc_list`: A list of Proc objects.
    * `descending`: Determines whether list should be in descending or ascending order(Default).

    Returns:

    A sorted list of `Proc` objects based on their `uptime`.
    """
    proc_list.sort(key=lambda proc: proc.uptime().sec, reverse=descending)
    return proc_list


def __get_valid_process(process: Process) -> Process:
    try:
        return process
    except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
        return None


def __conv_process_to_proc(process: Process) -> Proc:
    if __get_valid_process(process) is not None:
        return Proc(process)
    return None


def generate_proc_list(
    size: int, sortby: Function = sortby_mem_usage, descending: bool = True
) -> List[Proc]:
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
    proc_list: List[Proc] = [
        __conv_process_to_proc(process)
        for process in psutil.process_iter()
        if __get_valid_process(process) is not None
    ]

    return sortby(proc_list, descending)[:size]
