import functools
import sys
import typing as t

Function = t.Callable[..., t.Any]


def redirect_to_file(filename: str) -> t.Callable[[Function], Function]:
    def redirect_wrapper(func: Function) -> Function:
        @functools.wraps(func)
        def wrapper(*args: t.Any, **kwargs: t.Any) -> t.Any:
            orig_stdout = sys.stdout
            with open(filename, "a") as file:
                sys.stdout = file
                result = func(*args, **kwargs)
            sys.stdout = orig_stdout
            return result

        return wrapper

    return redirect_wrapper


@redirect_to_file("test.log")
def thingy() -> None:
    print("hello!")


@redirect_to_file("test.log")
def thingy_with_args(name: str) -> None:
    print(f"hello {name}!")


print(thingy)
thingy()
thingy_with_args("bob")
