"""
Functions to compute the lifepath, destiny, and soul urge number from a provided birthday and name.
"""
import helper


def clean_birthday(birthday) -> str:
    """
    Validates a birthday and removes any characters that are not digits.
    :param birthday: The birthday as entered, e.g. "1995-09-01".
    :return: Only the digits of the birthday, e.g. "19950901".
    :raises ValueError: If the birthday contains a written month or has no digits.
    """
    if helper.has_written_month(birthday):
        raise ValueError("Your birthday should not contain the written out month (Sep, Sept, September). Submit the date with numeric values only.")

    birthday_clean = helper.extract_numeric(birthday)
    if birthday_clean == "":
        raise ValueError("Invalid input. Enter a date in the format YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY.")
    return birthday_clean

def clean_name(full_name) -> str:
    """
    Removes any characters from a full name that are not letters or spaces.
    :param full_name: The full name as entered, e.g. "Mary-Jane O'Brien".
    :return: The cleaned name, e.g. "MaryJane OBrien".
    :raises ValueError: If the name contains no letters.
    """
    full_name_clean = helper.extract_characters(full_name)
    if full_name_clean == "":
        raise ValueError("Invalid input. Enter a full name that contains letters.")
    return full_name_clean

def calculate_lifepath(birthday) -> int:
    """
    Computes the lifepath number by adding all digits of the birthday and reducing to a single digit or master number.
    :param birthday: The birthday as entered, e.g. "1995-09-01".
    :return: The lifepath number, e.g. 7.
    :raises ValueError: If the birthday is invalid (see clean_birthday).
    """
    birthday_clean = clean_birthday(birthday)
    lifepath_number = int(helper.add_digits(birthday_clean))

    return lifepath_number

def calculate_destiny(full_name: str) -> int:
    """
    Computes the destiny number from all letters of a full name.
    Each name is converted and reduced on its own, then the name totals are added and reduced again.
    :param full_name: The full name as entered, e.g. "Jane Doe".
    :return: The destiny number, e.g. 9.
    :raises ValueError: If the name contains no letters.
    """
    full_name_clean = clean_name(full_name)
    names = full_name_clean.split(" ")

    name_numbers = []
    for name in names:
        name_digits = helper.convert_word_to_number(name, False)
        name_number = helper.add_digits("".join([str(n) for n in name_digits]))
        name_numbers.append(name_number)

    total = sum([int(n) for n in name_numbers])
    destiny_number = int(helper.add_digits(str(total)))

    return destiny_number


def calculate_soul_urge(full_name: str) -> int:
    """
    Computes the soul urge number from the vowels of a full name ("y" always counts as a vowel).
    Each name is converted and reduced on its own, then the name totals are added and reduced again.
    :param full_name: The full name as entered, e.g. "Jane Doe".
    :return: The soul urge number, e.g. 8.
    :raises ValueError: If the name contains no letters.
    """
    full_name_clean = clean_name(full_name)
    names = full_name_clean.split(" ")

    name_numbers = []
    for name in names:
        name_digits = helper.convert_word_to_number(name, True)
        name_number = helper.add_digits("".join([str(n) for n in name_digits]))
        name_numbers.append(name_number)

    total = sum([int(n) for n in name_numbers])
    soul_urge_number = int(helper.add_digits(str(total)))

    return soul_urge_number



if __name__ == '__main__':
    try:
        print("Enter your birthday (e.g. YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY):")
        birthday = input()

        print("Enter your full name:")
        full_name = input()

        number_lifepath = calculate_lifepath(birthday)
        number_destiny = calculate_destiny(full_name)
        number_soul_urge = calculate_soul_urge(full_name)

        print(f"\nYour lifepath number is {number_lifepath}: the {helper.get_number_meaning(number_lifepath)}.")
        print(f"Your destiny number is {number_destiny}: the {helper.get_number_meaning(number_destiny)}.")
        print(f"Your soul urge number is {number_soul_urge}: the {helper.get_number_meaning(number_soul_urge)}.")

    except ValueError as ve:
        print(ve)
