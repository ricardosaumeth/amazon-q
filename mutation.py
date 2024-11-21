def mutation(strings: list[str]) -> bool:
    if not isinstance(strings, list):
        raise ValueError("Input must be a valid array of strings")
    if not all(isinstance(x, str) for x in strings):
        raise ValueError("All elements must be valid strings")

    source, target = [s.lower() for s in strings]
    return all(char in source for char in target)


print(mutation(["Alien", "lien"]))  # true
print(mutation(["Alien", "Lien"]))  # true
print(mutation(["Hello", "hey"]))  # false
