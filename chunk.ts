const chunk = (numbers: number[], size: number): number[][] => {
  if (Array.isArray(numbers) && size) {
    return !numbers.length ? [] : [numbers.slice(0, size)].concat(chunk(numbers.slice(size), size))
  } else {
    throw new Error("Numbers must be a valid array of integers and size a valid integer");
  }
}


console.log(chunk([1, 2, 3, 4, 5], 2)) // [[1,2], [3,4], [5]]