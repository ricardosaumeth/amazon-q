def slasher(numbers: list[int], size:int)->list[int]:
  if not isinstance(numbers, list):
    raise ValueError("Numers must be all of type list")
  if not all(isinstance(x, int) for x in numbers):
    raise ValueError("All elments must be int")
  if not isinstance(size, int) or size < 0:
    raise ValueError("second paramenter must be a valid int")
  #return list(x for i,x in enumerate(numbers) if i >= size)
  return numbers[size:]

print(slasher([1, 2, 3], 2)) # [3]