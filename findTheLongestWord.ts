const findTheLongestWord = (source: string) => {
  if (typeof source !== "string") throw new Error("input must be a valid string");
  
  const longestWord = source.split(" ").reduce((longest: string, word) => word.length > longest.length ? word : longest, "")
  return [longestWord.length, longestWord]
}

console.log(findTheLongestWord("Ricardo Manuel Santana Saumeth"))