from bank import value

def test_normal():
    assert value('hello') == 0
    assert value('Hello') == 0

def test_h():
    assert value('hey') == 20
    assert value('Hey') == 20

def test_no_h():
    assert value("what's up?") == 100
    assert value("What's up?") == 100
