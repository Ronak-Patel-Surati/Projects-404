from numb3rs import validate


def test_numb3rs():
    assert validate("101.001.010.110") == True
    assert validate("11.23.191.22") == True
    assert validate("....") == False


def test_alphabets():
    assert validate("cat.001.dog.bee") == False
    assert validate("lion") == False


def test_others():
    assert validate("112.212.311") == False
    assert validate("1") == False
    assert validate("101.512.511.322") == False
