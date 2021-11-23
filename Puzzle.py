#author Kent Chau
#Algorithms 325
#fall 2021
# week 8
import heapq
from copy import deepcopy

def solve_puzzle(Board, Source, Destination):
    # print(f'board, source, destination = {Board, Source, Destination}')
    bb = deepcopy(Board)
    rows = len(bb)
    col = len(bb[0])
    x, y = Source
    rowq = [x]
    colq = [y]
    dx, dy = Destination
    paths = {}

    for i in range(len(bb)):
        for j in range(len(bb[0])):
            paths.update({(i, j): []})

    bb[x][y] = True
    visited = [Source]
    while len(rowq) > 0:
        # x = rowq.pop(0)
        # y = colq.pop(0)
        x = rowq.pop()
        y = colq.pop()

        if bb[dx][dy] is True:
            # break
            return visited
        if Board[x][y] == '#' or Board[dx][dy] == '#':
            return visited
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # for i in range(4):

        for i in directions:
            xx = x + i[0]
            yy = y + i[1]

            if xx < 0 or yy < 0:
                continue
            if xx >= len(bb) or yy >= len(bb[0]):
                continue
            if bb[xx][yy] is True:
                continue
            if bb[xx][yy] == '#':
                continue
            rowq.append(xx)
            colq.append(yy)
            bb[xx][yy] = True

            if (xx, yy) not in visited:
                visited.append((xx, yy))
            break

            # if (x, y) not in visited:
            #     visited.append((x, y))
                # bb[x][y] = True
        # if (x, y) not in visited:
        #     visited.append((x, y))
    # return visited
    return None

bb = [['-', '-', '-', '-', '-'],
         ['-', '-', '#', '-', '-'],
         ['-', '-', '-', '-', '-'],
         ['#', '-', '#', '#', '-'],
         ['-', '#', '-', '-', '-']]

# print(solve_puzzle(bb, (0, 0), (4, 0)))
