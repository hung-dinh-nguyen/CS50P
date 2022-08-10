from working import convert
import pytest

def test_incorrect_hours():
    with pytest.raises(ValueError):
        assert convert("13 PM to 13 AM")

def test_incorrect_minutes():
    with pytest.raises(ValueError):
        assert convert("8:60 AM to 4:60 PM")
def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_incorrect_format():
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")

"""
from working import convert
import pytest

def test_short_format():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 PM to 5 AM') == '21:00 to 05:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'
    assert convert('12 PM to 12 AM') == '12:00 to 00:00'


def test_long_format():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9:00 PM to 5:00 AM') == '21:00 to 05:00'
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert convert('12:00 PM to 12:00 AM') == '12:00 to 00:00'

def test_minutes():
    assert convert('9:30 PM to 5:30 AM') == '21:30 to 05:30'
    assert convert('9:15 AM to 5:15 PM') == '09:15 to 17:15'
    assert convert('12:30 PM to 12:30 AM') == '12:30 to 00:30'

def test_invalid():
    with pytest.raises(ValueError):
        assert convert('cat')
        assert convert('09:00 to 17:00')
        assert convert('12to12')
        assert convert('12PM to 12AM')
        assert convert('12 PM - 12 AM')
        assert convert('12:60 PM to 12:80 AM')
        assert convert('50 AM to 60 PM')
        assert convert('10:7 AM - 5:1 PM')
        assert convert('10:700 AM - 5:100 PM')
"""