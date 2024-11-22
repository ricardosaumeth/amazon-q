# def is_palindrome(string: str) -> bool:
#     if not isinstance(string, str) or not string:
#         raise ValueError("Please enter a valid string")

#     reversed_str_list = list(reversed(list(string)))
#     reversed_string = "".join(reversed_str_list)
#     return string.lower().strip() == reversed_string.lower().strip()


def is_palindrome(value: str) -> bool:
    sanitized_value = "".join(char.lower() for char in value if char.isalnum())
    return sanitized_value == sanitized_value[::-1]


print(is_palindrome("eye"))
print(is_palindrome("121"))
print(is_palindrome("Civic"))
print(is_palindrome("Noon"))
print(is_palindrome("DAD"))
print(is_palindrome("Ricardo"))
print(is_palindrome(""))
