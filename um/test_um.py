from um import count

def test_normal():
    assert count('um, thanks, um...') == 2
    assert count('Hello, There') == 0

def test_um_in_words():
    assert count('hum tum bum um') == 1
    assert count('hum tum bum') == 0

def test_case():
    assert count('Hum Tum Bum Um') == 1
    assert count('Hum Tum Bum') == 0
    assert count('um uM Um UM') == 4