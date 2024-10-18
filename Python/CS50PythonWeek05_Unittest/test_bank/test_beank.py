from bank import value #less memory usage for computing perhaps??

#using cs50 as cheet code type check50
def test_hello():
    assert value('hello') == '$0'

def test_h():
    assert value('h') == '$20'
    assert value('hey') == '$20'
    assert value("holay") == '$20'

def test_others():
    assert value('Ron') == '$100'
    assert value('Whats up') == '$100'

def test_random():
    assert value('WHAAT') == '$100'
    assert value('W000000') == '$100'
