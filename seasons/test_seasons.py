from seasons import birthday
from seasons import difference
from seasons import convert
import pytest

def test_words():
    assert convert(difference(birthday('1997-12-04'))) == 'Twelve million, nine hundred seventy-five thousand, eight hundred forty minutes'
    assert convert(difference(birthday('2000-01-01'))) == 'Eleven million, eight hundred eighty-four thousand, three hundred twenty minutes'

def test_format():
    with pytest.raises(ValueError):
        assert convert(difference(birthday('2004-22-01')))
        assert convert(difference(birthday('2004-12-50')))
