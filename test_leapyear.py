from leapyear import checkLeapYear

def test_leapYear_true():
    assert checkLeapYear(2024) == True

def test_leapYear_false():
    assert checkLeapYear(2023) == False

def test_leapYear_century_exception():
    assert checkLeapYear(2000) == True
    assert checkLeapYear(1900) == False