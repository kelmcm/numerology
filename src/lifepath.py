"""
Lifepath number.

Computes the lifepath number from a provided birthday.
"""
from constants import NUMBER_MEANING, MASTER_NUMBERS
from helper import extract_numeric, has_written_month


def calculate_lifepath():
    """
    Gathers input birthday from terminal and computes lifepath number.
    """
    print("What is your birthday (e.g. YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY)?")
    birthday = input()

    if has_written_month(birthday):
        raise ValueError("Your birthday should not contain the written out month (Sep, Sept, September). Submit the date with numeric values only.")

    birthday_clean = extract_numeric(birthday)
    if birthday_clean == "":
        raise ValueError("Invalid input. Enter a date in the format YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY.")

    lifepath_number = int(add_digits(birthday_clean))

    meaning = NUMBER_MEANING.get(lifepath_number)
    print(f"\nYour lifepath number is {lifepath_number}: the {meaning}.")


def add_digits(string_number: str):
    """
    Recursive function to add the digits of a string number together until the final number is a single digit or a master number.
    """
    # If number is down to a single digit or master number, exit
    if len(string_number) <= 1 or int(string_number) in MASTER_NUMBERS:
        return string_number
    # Else, split digits and add
    else:
        digits = list(string_number)
        print(" + ".join(digits))

        total = 0
        for d in digits:
            total += int(d)

        print("= ", total)
        return add_digits(str(total))


if __name__ == '__main__':
    try:
        calculate_lifepath()
    except ValueError as ve:
        print(ve)
