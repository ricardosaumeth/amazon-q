type innerArray = [number, number, number, number]
type numbers = innerArray[]

const largestOfFour = (numbers: numbers) => {
  if (!Array.isArray(numbers) || numbers.length !== 4 || !numbers.every(isValidInnerArray)) {
    throw new Error("Please check the input");
  }

  return numbers.map(findLargestNumber)
}

const isValidInnerArray = (numbers: number[]) =>
  Array.isArray(numbers) && numbers.length === 4 && numbers.every(x => typeof x === "number")

const findLargestNumber = (numbers: number[]) => Math.max(...numbers)

console.log(largestOfFour([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])) // [4, 8, 12, 16]