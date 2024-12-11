const titleCase = (string: string) => {
  if (!string.trim().length) {
    throw new Error("Input not valid");
  }
  return string.toLowerCase().split(" ").map(x => x.at(0)?.toUpperCase() + x.slice(1)).join(" ")
}

console.log(titleCase("I'm a little tea pot")) // I'm A Little Tea Pot