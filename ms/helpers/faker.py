import random
from datetime import date


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_random_letters(length):
    char = ""
    for i in range(0, length):
        index = random.randint(0, len(letters) - 1)
        char += letters[index]
    return char


def get_random_letters_with_numbers(length):
    char = ""
    chars = letters + numbers
    for i in range(length):
        randint = random.randint(0, len(chars) - 1)
        char += str(chars[randint])
    return char


def birthday():
    current_year = date.today().year
    year = random.randint(current_year - 100, current_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"


def name_birthday(name: str = None, lastname: str = None, second_lastname : str = None, birthday: str = birthday):
    prefix = get_random_letters(2) if lastname is None else lastname[:2]
    prefix += get_random_letters(1) if second_lastname is None else second_lastname[:1]
    prefix += get_random_letters(1) if name is None else name[:1]

    birthday = birthday if isinstance(birthday, str) else birthday()
    birthday = birthday.split("-")
    prefix += birthday[0][2:]
    prefix += birthday[1]
    prefix += birthday[2]

    return prefix


def rfc(name: str = None, lastname: str = None, second_lastname : str = None, birthday: str = birthday):
    rfc = name_birthday(name, lastname, second_lastname, birthday)
    rfc += get_random_letters_with_numbers(3)
    return rfc.upper()


def curp(name: str = None, lastname: str = None, second_lastname : str = None, birthday: str = birthday, entity_birth: str = None, gender: str = None):
    curp = name_birthday(name, lastname, second_lastname, birthday)
    curp += gender or random.choice(["H", "M"])
    curp += entity_birth or get_random_letters(2)
    curp += get_random_letters_with_numbers(5)
    return curp.upper()
