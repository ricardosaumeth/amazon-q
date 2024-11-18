const mutation = (strings: string[]) => {
  if (!Array.isArray(strings) || strings.length !== 2)
    throw new Error("input must be a valid array of string")

  const [source, target] = strings;
  return target.split("").every(s => source.includes(s))
}

console.log(mutation(["Alien", "lien"]))
console.log(mutation(["Hello", "hey"]))