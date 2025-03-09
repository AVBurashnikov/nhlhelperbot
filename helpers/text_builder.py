from typing import Tuple, List, Any, Optional, Callable


def text(
        value: Any | List[Any] = "",
        pre: Optional[str] = None,
        post: Optional[str] = None,
        fmt_func: Optional[Callable[[str], str] | Tuple[Callable[[str], str], ...]] = None,
        sep: str = " ",
        new_line: int = 0
) -> str:
    res = sep.join(map(str, value)) if isinstance(value, List) else str(value)

    res = f"{pre}" + res if pre else res

    res = res + f"{post}" if post else res

    if callable(fmt_func):
        return fmt_func(res) + "\n" * new_line

    if isinstance(fmt_func, Tuple):
        for func in fmt_func:
            if not callable(func):
                raise TypeError("fmt_func must be either a callable or a tuple of callables.")
            res = func(res)

    return res + "\n" * new_line
