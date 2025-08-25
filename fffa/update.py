import random

def update_Foxes(data, M, N, V, g, G, leader, leader_num, history, h_best, w=0.5, c1=1, c2=1):
    r1 = random.randint(0, 10) / 10
    r2 = random.randint(0, 10) / 10
    r3 = random.randint(-1, 1)

    for i in range(M):
        for j in range(N):
            social = leader[j] - data[i][j]
            cog = history[h_best][i][j] - data[i][j]
            c3 = c1 * G / (g + 1)
            c4 = c2 * G / (g + 1)

            V[i][j] = w * V[i][j] + (c3 * r1 * r3 * social) + (c4 * r2 * cog)
            data[i][j] = int(data[i][j] + V[i][j]) % N

    return data
