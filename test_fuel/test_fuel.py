from fuel import convert
from fuel import gauge
import pytest


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_non_integer():
    with pytest.raises(ValueError):
        convert('A/B')

def test_gauge_value():
    assert gauge(convert('1/2')) == '50%'
    assert gauge(convert('1/4')) == '25%'
    assert gauge(convert('1/1')) == 'F'
    assert gauge(convert('99/100')) == 'F'
    assert gauge(convert('0/1')) == 'E'
    assert gauge(convert('1/100')) == 'E'