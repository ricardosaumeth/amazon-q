const addToguether = (first: number) => {
  validateNumber(first, "first")

  return (second: number) => {
    validateNumber(first, "second")
    return first + second
  }
}

const validateNumber = (number: number, position: string) => {
  if (typeof number !== "number" || Number.isNaN(number))
    throw new Error(`${position} must be a valid number`)
}


console.log(addToguether(2)(30))