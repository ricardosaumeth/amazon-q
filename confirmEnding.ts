const confirmEnding = (source: string, endWord: string) => {
  const isString = (value: unknown): value is string => typeof value === "string" && value.trim().length > 0;
  if (!isString(source) || !isString(endWord)) {
    throw new Error("Both source and endWord must be valid strings");
  }
  return source.endsWith(endWord);
}

console.log(confirmEnding("Ricardo Manuel Santana Saumeth", "Saumeth"))
console.log(confirmEnding("Ricardo Manuel Santana Saumeth", "SaumethX"))
console.log(confirmEnding("", ""))