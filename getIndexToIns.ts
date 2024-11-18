const getIndexToIns = (numbers: number[], n: number) => {
  validateInputs(numbers, n)
  
  return numbers.findIndex(x => x > n) !== -1 ? numbers.findIndex(x => x > n) : numbers.length
}

export const validateInputs = (numbers: number[], number: number) => {
  if (!Array.isArray(numbers) || !Number.isFinite(number)) { // is either integer or float
    throw new Error("Input are not valid");
  }
}

const isFloat = (n: number) => Number.isFinite(n) && !Number.isInteger(n); // only works for floats


console.log(getIndexToIns([1, 2, 3, 4], 1.5))//1