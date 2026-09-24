import helper
import pytest

@pytest.mark.parametrize("input_string, expected", [
    ("1994-08-01", "19940801"),
    ("08/01/1994", "08011994"),
    ("08011994", "08011994"),
    ("1994 08 01", "19940801"),
    ("hello", ""),
    ("", "")
])
def test_extract_numeric(input_string, expected):
    assert helper.extract_numeric(input_string) == expected


@pytest.mark.parametrize("date_string, expected", [
    ("Sept 1, 1995", True),
    ("September 1 1995", True),
    ("1 jan 1990", True),
    ("1995-09-01", False),
    ("19950901", False),
    ("hello", False),
    ("", False)
])
def test_has_written_month(date_string, expected):
    assert helper.has_written_month(date_string) == expected
