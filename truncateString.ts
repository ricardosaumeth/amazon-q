const truncateString = (string: string, size: number) => {
  if (!isValidString(string)) {
    throw new Error("String is not valid");
  }

  if (!isIntegerValid(size)) {
    throw new Error("Size input is not vald");
  }

  return string.length !== size ? string.slice(0, size > 3 ? size - 3 : size) + "..." : string
}

const isValidString = (string: string) => typeof string === "string" && string.trim().length

const isIntegerValid = (number: number) => Number.isInteger(number)

console.log(truncateString("A-tisket, a-tasket A green and yellow basket",
  "A-tisket, a-tasket A green and yellow basket".length)); //A-tisket, a-tasket A green and yellow basket
console.log(truncateString("A-tisket, a-tasket A green and yellow basket", 11)); // A-tisket...
console.log(truncateString("A-tisket...", 1));// A...