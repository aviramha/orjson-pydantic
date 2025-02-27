import orjson
import pytest


@pytest.mark.parametrize("input", [
    b'"\xc8\x93',
    b'"\xc8',
])
def test_invalid(input):
    with pytest.raises(orjson.JSONDecodeError):
        orjson.loads(input)
