from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert print(jar) == None
    assert str(jar.capacity) == '12'
    assert str(jar.size) == '0'

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == '🍪'

    jar.deposit(5)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'

def test_too_much_cookies():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(6)

def test_not_enough_cookies():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(1)

def test_invalid_capacity():
    with pytest.raises(ValueError):
        jar = Jar(-1)