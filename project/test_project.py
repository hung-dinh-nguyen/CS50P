from project import input_check, roman_convert, combine
import pytest

def test_input_check():
    assert input_check('5') == 5
    assert input_check('12345') == 12345

def test_words():
    with pytest.raises(ValueError):
        assert input_check('cat')
        assert input_check('dog')
        assert input_check('1234 123 2')

def test_roman_convert():
    assert roman_convert(5) == ['V']
    assert roman_convert(1234) == ['M', 'C', 'C', 'X', 'X', 'X', 'IV']
    assert roman_convert(129) == ['C', 'X', 'X', 'IX']

def test_combine():
    assert combine(['V']) == 'V'
    assert combine(['M', 'C', 'C', 'X', 'X', 'X', 'IV']) == 'MCCXXXIV'
    assert combine(['C', 'X', 'X', 'IX']) == 'CXXIX'