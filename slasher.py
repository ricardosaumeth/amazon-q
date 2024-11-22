def slasher(numbers: list[int], size:int)->list[int]:
  if size < 0:
    raise ValueError("Size must be greater than zero")
  #return list(x for i,x in enumerate(numbers) if i >= size)
  return numbers[size:]

print(slasher([1, 2, 3], 2)) # [3]