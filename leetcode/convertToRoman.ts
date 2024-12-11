const convertToRoman = (number: number) => {
  if (typeof number !== "number" || number < 1 || !Number.isInteger(number)) {
    throw new Error("Input must be a positive integer");
  }
  const romanNumeralMap: [number, string][] = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I']
  ]
  let result = ""
  for (const [value, symbol] of romanNumeralMap) {
    while (number >= value) {
      number -= value
      result += symbol
    }
  }
  return result
}


console.log(convertToRoman(83));// should return "LXXXIII"
console.log(convertToRoman(3999));// should return "MMMCMXCIX
console.log(convertToRoman(2));// should return "II".
console.log(convertToRoman(3));// should return "III".
console.log(convertToRoman(4));// should return "IV".
console.log(convertToRoman(5));// should return "V".