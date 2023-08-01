import pytest

import application


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Ed", "Hello Ed"),
    ],
)
def test_hello(name, expected):
    result = application.hello(name=name)
    assert result == expected


def test_value_error():
    with pytest.raises(application.NotAStringError):
        _ = application.hello(name=1)
