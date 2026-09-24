import numerology
import pytest


@pytest.mark.parametrize("birthday, expected", [
    ("1995-09-01", "19950901"),
    ("09/01/1995", "09011995"),
    ("19950901", "19950901")
])
def test_clean_birthday(birthday, expected):
    assert numerology.clean_birthday(birthday) == expected

@pytest.mark.parametrize("birthday", [
    "Sept 1, 1995",
    "hello",
    ""
])
def test_clean_birthday_invalid(birthday):
    with pytest.raises(ValueError):
        numerology.clean_birthday(birthday)

@pytest.mark.parametrize("birthday, expected", [
    ("1995-09-01", 7),
    ("09/01/1995", 7),
    ("01/09/1995", 7),
    ("2025-03-15", 9),
    ("2009-09-09", 11)
])
def test_calculate_lifepath(birthday, expected):
    assert numerology.calculate_lifepath(birthday) == expected

@pytest.mark.parametrize("full_name, expected", [
    ("Jane Doe", 9),
    ("JANE DOE", 9),
    ("Jane Mary Doe", 3),
    ("Jane Bo", 11),
    ("A J", 2),
    ("K K", 4),
    ("Mary-Jane Doe", 3),
    ("O'Brien Smith", 6)
])
def test_calculate_destiny(full_name, expected):
    assert numerology.calculate_destiny(full_name) == expected

@pytest.mark.parametrize("full_name, expected", [
    ("Jane Doe", 8),
    ("JANE DOE", 8),
    ("Jane Mary Doe", 7),
    ("A A", 2),
    ("Lynn Doe", 9),
    ("Lynn Wynn", 5),
    ("Mary-Jane Doe", 7)
])
def test_calculate_soul_urge(full_name, expected):
    assert numerology.calculate_soul_urge(full_name) == expected
