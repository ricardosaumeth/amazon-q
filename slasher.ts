const slasher = (numbers: number[], size: number) => {
  if (!isValidInput(numbers, size)) {
    throw new Error("Input are not vald");
  }
  return numbers.slice(size)
}

const isValidInput = (numbers: number[], size: number) =>
  Array.isArray(numbers) &&
  numbers.length === 3 &&
  numbers.every(x => typeof x === "number") &&
  Number.isInteger(size)

console.log(slasher([1, 2, 3], 2))//[3]