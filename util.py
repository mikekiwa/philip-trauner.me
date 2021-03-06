from typing import Callable, List, Tuple, Type, Dict, Any, Union, Iterable
from sys import exc_info
from traceback import print_exception

WARNING_COLOR = "\033[33m"
EMPHASIS_COLOR = "\033[35m"
ANSI_END = "\033[0m"


def safe_execute(default: Any, exception: Any, function: Callable, *args: Any):
    try:
        return function(*args)
    except exception:
        return default


def warning(text: str) -> None:
    print("%sWARNING%s: %s" % (WARNING_COLOR, ANSI_END, text))


def info(text: str) -> None:
    print("%sINFO%s: %s" % (EMPHASIS_COLOR, ANSI_END, text))


def all_match_condition(function: Callable, iterable: Iterable) -> bool:
    for element in iterable:
        if not function(element):
            return False
    return True


def capture_trace():
    exc_type, exc_value, exc_traceback = exc_info()
    print_exception(exc_type, exc_value, exc_traceback)


def index_range_from_pair(iterable: Iterable, pair: Tuple[int, int]):
    return iterable[pair[0] : pair[1]]


def traverse_collection(collection: Union[List, Dict], index: List[Any]):
    result = collection

    for index_ in index:
        result = result[index_]

    return result
