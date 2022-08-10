from plates import is_valid

def test_starts_2_letters():
    assert is_valid('CS50') == True
    assert is_valid('PAT') == True
    assert is_valid('PAT2') == True
    assert is_valid('05C') == False

def test_length_limit():
    assert is_valid('C') == False
    assert is_valid('H') == False
    assert is_valid('PATRICK') == False
    assert is_valid('OUTATIME') == False

def test_order():
    assert is_valid('CS50SC') == False
    assert is_valid('A22A') == False
    assert is_valid('CS50P') == False

def test_first_zero():
    assert is_valid('CS05') == False
    assert is_valid('JB007') == False

def test_with_non_alphanumerical():
    assert is_valid('Hello, World') == False
    assert is_valid('-S50') == False
    assert is_valid('*p50') == False
    assert is_valid('!C!') == False
    assert is_valid('@C50') == False
    assert is_valid('PI3.14') == False

def test_no_alphanumerical():
    assert is_valid(' ') == False
    assert is_valid('__') == False
    assert is_valid('..') == False
    assert is_valid('') == False


def test_start_numbers():
    assert is_valid('0000') == False
    assert is_valid('1111') == False

def test_alphanumeric_characters():
    assert is_valid("AA") == True
    assert is_valid("aa") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False
    assert is_valid('PAT2') == True
    assert is_valid('PAT234') == True

