from bank import value

def main():
    test_20_result()
    test_0_result()
    test_100_result()


def test_20_result():
    assert value("h") == 20
    assert value("hey") == 20
    assert value("how are you") == 20

def test_0_result():
    assert value("hello") == 0
    assert value("HELLO gi") == 0
    assert value("Hello How are you") == 0


def test_100_result():
    assert value("what's up") == 100
    assert value("Good morning") == 100
    assert value("Good evening") == 100


if __name__ == "__main__":
    main()
