const validateInputs = (numbers: number[], target: number) => {
  if (!Array.isArray(numbers) || !Number.isFinite(target)) {
    throw new Error("Inputs must be valid");

  }
}

const binarySearch = (numbers: number[], target: number) => {
  validateInputs(numbers, target)
  numbers = numbers.sort((a, b) => a - b)
  let left = 0
  let right = numbers.length - 1
  while (left <= right) {
    const mid = Math.floor(left + right / 2)
    if (numbers[mid] === target) return mid
    else if (numbers[mid] < target) left++
    else right--
  }
  return -1
}

console.log(binarySearch([1, 2, 3, 49, 5], 49))

