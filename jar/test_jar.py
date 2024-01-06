from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-22)


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(1)
    assert jar.cookies == 10
    with pytest.raises(ValueError):
        jar.withdraw(85) == ""


def test_str():
    jar = Jar()
    assert str(jar) == ""
