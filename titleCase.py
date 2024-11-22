# def title_case(string: str) -> str:
#     if not string:
#         return string
#     result = ""
#     for j in string.split(" "):
#         result += j[0].upper() + j[1:] + " "

#     return "".join(result)


def title_case(string: str) -> str:
    if not string.strip():
        raise ValueError("Input not valid")

    return " ".join(word[0].upper() + word[1:] for word in string.lower().split())


print(title_case("I'm a little tea pot"))  # I'm A Little Tea Pot
