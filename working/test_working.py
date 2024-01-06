
from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_invalid():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_value_range():
    with pytest.raises(ValueError):
        assert convert("8:60 AM to 9:60 PM")

def test_value_omits():
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")

def 