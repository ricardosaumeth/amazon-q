const addToguether = (a: number): ((b: number) => number | undefined) => (b: number) => typeof b !== "number" ? undefined : a + b

console.log(addToguether(2)(3))