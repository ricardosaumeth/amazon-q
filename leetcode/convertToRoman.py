from typing import Tuple


def convert_to_roman(number: int) -> str:
    if number < 1:
        raise ValueError("Input must be a positive integer")

    roman_numeral_map: list[Tuple[int, str]] = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for value, symbol in roman_numeral_map:
        while number >= value:
            number -= value
            result += symbol
    return result


print(convert_to_roman(83))  # should return "LXXXIII"
print(convert_to_roman(3999))  # should return "MMMCMXCIX
print(convert_to_roman(2))  # should return "II".
print(convert_to_roman(3))  # should return "III".
print(convert_to_roman(4))  # should return "IV".
print(convert_to_roman(5))  # should return "V".
