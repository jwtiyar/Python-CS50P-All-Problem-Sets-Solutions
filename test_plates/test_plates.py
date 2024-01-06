from plates import is_valid

def test_no_alphabetical():
    assert is_valid("8055") == False
    #No alphabetical check

def test_length():
    assert is_valid("hggfgfggfgfgfh") == False
    assert is_valid("h") == False
    ## length check

def test_first_num_zero():
    assert is_valid("dd02") == False
    assert is_valid("0hhkl") == False
    ## zero placemnt

def test_num_in_middle():
    assert is_valid("gg11kk") == False
    assert is_valid("cs50p") == False
    ## Number placemnt

def test_no_punctuation():
    assert is_valid(",g,f.hh") == False

def test_alpha_numeric():
    assert is_valid("PI3.14") == False
    ## alpha numeric

def test_Capital():
    assert is_valid("HIHIHIR") == False
    assert is_valid("CS2323") == True

