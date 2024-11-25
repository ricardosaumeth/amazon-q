const validateInputs = (numbers: number[], target: number) => {
  if (!Array.isArray(numbers) || !Number.isFinite(target)) {
    throw new Error("Inputs must be valid");

  }
}

const binarySearch = (numbers: number[], target: number) => {
  validateInputs(numbers, target)
  let left = 0
  let right = numbers.length - 1
  while (left <= right) {
    const mid = Math.floor((left + right) / 2)
    if (numbers[mid] === target) return mid
    else if (numbers[mid] < target) left = mid + 1
    else right = mid - 1
  }
  return -1
}

console.log(binarySearch([1, 2, 3, 49, 5], 49)) // 3
console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) // 4
