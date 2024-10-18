from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('Hello') == 0
    assert value('hello, world') == 0

def test_haa():
    assert value('h') == 20
    assert value('hey') == 20
    assert value('holay') == 20

def test_others():
    assert value('Ron') == 100
    assert value('Whats up') == 100

def test_random():
    assert value('WHAAT') == 100
    assert value('W000000') == 100

def test_hello():
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('Hey') == 20
