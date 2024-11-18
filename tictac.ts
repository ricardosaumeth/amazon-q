type CellValue = 'X' | 'O'

type Board = {
  [key: number]: CellValue
}

type WinningCombination = [number, number, number]
type WinningCombinations = WinningCombination[]

const winCombo: WinningCombinations = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [1, 5, 9],
  [7, 5, 3],
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9],
]

const board: Board = {
  1: 'X',
  2: 'X',
  3: 'X',
  4: 'O',
  5: 'O',
  6: 'X',
  7: 'X',
  8: 'O',
  9: 'O',
}

type WinningCombo = {
  board: Board
  symbol: string
}

const isWinningCombo = ({
  board,
  symbol,
}: WinningCombo): [boolean, WinningCombination | null] => {
  for (const combo of winCombo) {
    if (combo.every(x => board[x] === symbol)) {
      return [true, combo]
    }
  }
  return [false, null]
}

console.log(isWinningCombo({ board, symbol: "X" })) // true, [1,2,3]
