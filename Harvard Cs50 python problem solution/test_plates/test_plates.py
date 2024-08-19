from plates import is_valid

def main():
    test_min_max()
    test_two_letter()
    test_middle_number()
    test_num_zero()
    test_punnctutaion()

#plates must be between 2 and 6 characters: defines the minimum and maximum length.
def test_min_max():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False

#checkingg valid plates input and it should be at least 2 letters
def test_two_letter():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

#number cannot be use in middle of a plats they must place at the end
def test_middle_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

#check first number cannot be a 0
def test_num_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


#no periods, spaces, or punctuation marks are allowed
def test_punnctutaion():
    assert is_valid("PI#.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI 14") == False

if __name__ == "__main__":
    main()
