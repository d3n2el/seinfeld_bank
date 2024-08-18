from bank import value
def main():
    test_value()
    test_numbers()
    test_uppercase()

def test_value():
    assert value("Hello") == "$0"
    assert value("hi") == "$20"
    assert value("greetings") == "$100"

def test_numbers():
    assert value("1") == "$100"
    assert value("12") == "$100"
    assert value("123") == "$100"
    assert value("1234") == "$100"

def test_uppercase():
    assert value("HELLO") == "$0"
    assert value("HI") == "$20"
    assert value("GREETINGS") == "$100"

if __name__ == "__main__":
    pytest.main()
