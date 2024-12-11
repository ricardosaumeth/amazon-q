const factorialize = (number: number): number => {
  if (typeof number !== "number" || number < 0) {
    throw new Error("Input must be a non-negative integer");
  }

  return number <= 1 ? 1 : number * factorialize(number - 1);
};

console.log(factorialize(5))