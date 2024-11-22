def mutation(strings: list[str]) -> bool:
    source, target = [s.lower() for s in strings]
    return all(char in source for char in target)


print(mutation(["Alien", "lien"]))  # true
print(mutation(["Alien", "Lien"]))  # true
print(mutation(["Hello", "hey"]))  # false
