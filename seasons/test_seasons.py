import pytest
from seasons import minutesDate
from seasons import ChangeToWords

# def test_get_minutes():
#     assert minutesDate()

def test_change_word():
    assert ChangeToWords(52) == "fifty-two"