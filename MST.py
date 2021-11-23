#author Kent Chau
#algo 325
#fall 2021
#homework 8

#reference exploration module eight: prim's algorithm
def Prims(G):
    inf = 9999999
    V= len(G)
    g2 = []
    for i in range(len(G)):
        g2 += [0*(len(G))]

    selected = [0]*(len(G))
    no_edge = 0
    selected[0] = True
    # print("edge: weight\n")
    listTup = []
    while (no_edge < V -1):
        minimum = float("inf")
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if((not selected[j] and G[i][j])):
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        listTup.append((x, y, G[x][y]))
        selected[y] = True

        no_edge += 1
    return listTup