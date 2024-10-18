from plates import is_valid
#check for len
#check for startletter??
#check for numberlats??
#check for characterless personaassssssss?


def test_len():
    assert is_valid('aa') == True
    assert is_valid('vandebharat123') == False
    assert is_valid('gatian123') == False

def test_startletter():
    assert is_valid('ABB') == True
    assert is_valid('a123') == False
    assert is_valid('z2') == False

def test_num():
    assert is_valid('st2udn') == False
    assert is_valid('fn4ign') == False
    assert is_valid('se001') == False


def test_alphanumb():
    assert is_valid('AAABBCd') ==False
    assert is_valid('123456') ==False


def test_notalphanumeric():
    assert is_valid('!@#$$') == False



