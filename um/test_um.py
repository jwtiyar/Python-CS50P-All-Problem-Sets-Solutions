from um import count

def test_count():
    assert count("um ") == 1

def test_symbol():
    assert count("Um?") == 1

def test_sentence():
    assert count("1um ") == 0