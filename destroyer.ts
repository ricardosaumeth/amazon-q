const areAllIntegers = (...args: number[]) => args.every(x => Number.isInteger(x))

const destroyer = (numbers: number[], target1: number, target2: number) => {
  if (!Array.isArray(numbers))
    throw new Error("First input must be a valid array of numbers")

  if (!areAllIntegers(target1, target2)) {
    throw new Error("Second and third input must be valid numbers")
  }

  return numbers.filter(x => x !== target1 && x !== target2)
}

console.log(destroyer([1, 2, 3, 1, 2, 3], 2, 3))