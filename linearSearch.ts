const linearSeach = (numbers: number[], target: number) => {
  validateInputs(numbers, target)
  return numbers.findIndex(x => x === target)
}


console.log(linearSeach([1,2,3,49,5], 490))

export const validateInputs = (numbers: number[], target: number) => {
  if(!Array.isArray(numbers) || !Number.isFinite(target)) {
    throw new Error("Inputs must be valid");
    
  }
}
