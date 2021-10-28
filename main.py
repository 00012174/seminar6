def test_is_valid(test):
    if (isinstance(test, int)==True) and (1<= test <=3):
        return True
    else:
        return False
print(test_is_valid(2))
print(test_is_valid("ryhrh"))
print(test_is_valid(7))

