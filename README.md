# Block_Puzzle_Algorithm

problem: You are given a 2D puzzle of size MxN, that has N rows and M columns (N>=3; M>=3; M and N can be different). Each cell in the puzzle is either
empty or has a barrier. An empty cell is marked by '-' (hyphen) and the one with a barrier is marked by '#'. You are given two coordinates from the puzzle (a, b)
and (x, y). You are currently located at (a, b) and want to reach (x, y). You can move only in the following directions.

L: move to the left cell from the current cell
R: move to right cell from the current cell
U: move to upper cell from the current cell
D: move to the lower cell from the current cell

You can move to only an empty cell and cannot move to a cell with a barrier (#) in it. Your goal is to find the minimum number of cells that you have to cover to reach 
the destination cell (do not count the starting cell and the destination cell) in the form of a list of coordinates. The coordinates (1, 1) represent the first cell; (1, 2) represent the second cell in the first row. If there is no possible path from source teo destination return 'None.'

Input board:
[-, -, -, -, -]
[-, -, #, -, -]
[-, -, -, -, -]
[#, -, #, #, -]
[-, #, -, -, -]

Example: (a, b): (0, 0); (x, y): (3,3)
        
        output:
        [(0, 0, (0, 1), (0, 2), (0, 3), (0, 4), (2, 4), (2, 4), (3, 4), (4, 4)]
        
Notes: implementation of breadth first search is the best approach since we are trying to get to the end in min number of coordinates. Found a more efficient way to
implement L, R, U, D, instructions, imported and used DeepCopy to copy the board since the board was not being persistent. Used an iterative approach. 
