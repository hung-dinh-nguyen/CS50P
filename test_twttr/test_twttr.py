from twttr import shorten

def test_lowercase():
    assert shorten('apple') == 'ppl'
    assert shorten('teams') == 'tms'

def test_uppercase():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('WATER') == 'WTR'

def test_combo():
    assert shorten('FabULOus') == 'FbLs'
    assert shorten('aWOl') == 'Wl'

def test_no_vowel():
    assert shorten('rhythm') == 'rhythm'

def test_numbers():
    assert shorten('CS50') == 'CS50'

def test_punctuation():
    assert shorten('...Please...') == '...Pls...'