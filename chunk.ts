const chunk = (numbers: number[], size: number): number[] =>
  !numbers.length ? [] : numbers.slice(0, size).concat(chunk(numbers.slice(size), size))

console.log(chunk([1, 2, 3, 4, 5], 2))