from twttr import shorten

def test_main():
    test_check_upper()
    test_check_lower()
    test_check_num()
    test_check_symbl()


def test_check_upper():
    assert shorten('TWITTER') == 'TWTTR'

def test_check_lower():
    assert shorten('twitter') == 'twttr'

def test_check_num():
    assert shorten('123') == '123'

def test_check_symbl():
    assert shorten('!?.,') == '!?.,'


# if __name__ == "__main__":
#     main()
