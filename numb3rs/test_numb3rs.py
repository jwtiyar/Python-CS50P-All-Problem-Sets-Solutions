
from numb3rs import validate


def test_validate():
    assert validate("255.255.255.0") == True

def test_Nonumber():
    assert validate("cat") == False

def test_longip():
    assert validate("192.168.1.1.1") == False

def test_inrange():
    assert validate("192.266.300.266") == False