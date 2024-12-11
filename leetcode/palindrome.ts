// const isPalindrome = (
//   value: string,
//   sanitize: (s: string) => string = (s) => s.toLowerCase().replace(/[^a-z0-9]/g, '')
// ): boolean => {
//   const sanitizedValue = sanitize(value);
//   return sanitizedValue === sanitizedValue.split('').reverse().join('');
// };

const isPalindrome = (value: string): boolean => {
  const sanitizedValue = value.toLowerCase().replace(/[^A-z0-9]/g, "")
  return sanitizedValue === sanitizedValue.split("").reverse().join("")
};

console.log(isPalindrome("eye"))
console.log(isPalindrome("121"))
console.log(isPalindrome("Civic"))
console.log(isPalindrome("Noon"))
console.log(isPalindrome("DAD"))
console.log(isPalindrome("Ricardo"))