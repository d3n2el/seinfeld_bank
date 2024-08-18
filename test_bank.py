from bank import value

def test_0():
    assert value("hello") == 0

def test_20():
    assert value("hi") == 20
    assert value("hurray") == 20
    assert value("how you doing") == 20

def test_100():
    assert value("1") == 100
    assert value("12") == 100
    assert value("what's up") == 100
    assert value("greetings") == 100

def test_uppercase():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("GREETINGS") == 100

