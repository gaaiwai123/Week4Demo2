 from typing import List


board = [
    "... ...................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:

    # Implement your code here.

    i,j = len(input_board), len(input_board[0])
    if input_board[x][y]==new:
        return input_board

    def find(m,n):
        if input_board[m][n]==old:
            input_board[m] = input_board[m][:n] + new + input_board[m][n + 1:]
            if m>=1:
                find(m-1,n)
            if m+1 < i:
                find(m+1,n)
            if n>=1:
                find(m,n-1)
            if n+1< j:
                find(m,n+1)

    find(x, y)

    return input_board
    
modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)
    