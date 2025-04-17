def triangle(G):
    n = len(G)

    for u in range(n):
        for v in range(n):
            if u != v and G[u][v] == 1:
                for w in range(n):
                    if w != u and w != v:
                        if G[u][w] == 1 and G[v][w] == 1:
                            return True
    return False