from leapyear import leap_year

def test_leap_year():
    assert leap_year(2024) == True

def test_not_leap_year():
    assert leap_year(2025) == False

def test_leap_year_2():
    assert leap_year(2000) == True

def test_not_leap_year_2():
    assert leap_year(1900) == False