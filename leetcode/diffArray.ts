const diffArray = (array1: number[], array2: number[]) => {
  validateInput(array1)
  validateInput(array2)

  const [smallestArray, largestArray] = array1.length <= array2.length ? [array1, array2] : [array2, array1]
  return largestArray.filter(x => !smallestArray.includes(x))
}

export const validateInput = (array1: number[]) =>
  !Array.isArray(array1) || typeof array1 !== "number"
//||!array1.every(x => typeof x !== "number")

console.log(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]))// 4