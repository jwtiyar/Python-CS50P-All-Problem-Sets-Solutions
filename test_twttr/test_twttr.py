from twttr import shorten

def main():
    test_shorten()

def test_shroten():
    assert shorten("hii") == "h"
def test_capital():

    assert shorten("ROHan") == "RHn"
    assert shorten("12ADDU") == "12DD"
    assert shorten(",,,,RuODi") == ",,,,RD"
if __name__ == "__main__":
    main()