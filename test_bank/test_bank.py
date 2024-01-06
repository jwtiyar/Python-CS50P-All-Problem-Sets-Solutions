from bank import value

def test_value():
    assert value("hey") == 20
    assert value("hello") == 0
    assert value("Hello") == 0
def test_h():
    assert value("httthyy") == 20
def test_others():
    assert value("Rohan") == 100
