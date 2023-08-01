class NotAStringError(ValueError):
    pass


def hello(name: str = "") -> str:
    if not type(name) == str:
        raise NotAStringError
    return f"Hello {name}"
