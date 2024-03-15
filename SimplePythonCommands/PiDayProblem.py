def find_f_g(n):
    f_n_minus_1 = 1/6
    g_n_minus_1 = 1/30
    f_n, g_n = 0  , 0
    for i in range (2, n +1):
        f_n = f_n_minus_1 + (1 /( i * (4 * i  - 1) * (4 * i - 2)))  
        g_n = g_n_minus_1 + (1 /( i * (4 * i  + 1) * (4 * i + 2)))
        f_n_minus_1, g_n_minus_1 = f_n, g_n
    return f_n , g_n

F , G = find_f_g(2024)
print(F)
print(G)
results = F + 3 - G

print(f"Happy {results} Day!!!")


def find_f_g2(n):
    f_n_minus_1 = 1/6
    g_n_minus_1 = 1/30
    f_n, g_n = 0, 0
    for i in range(2, n + 1):
        f_n = f_n_minus_1 + (1 / (i * (4 * i - 1) * (4 * i - 2)))
        g_n = g_n_minus_1 + (1 / (i * (4 * i + 1) * (4 * i + 2)))
        f_n_minus_1, g_n_minus_1 = f_n, g_n
    return f_n, g_n

F2, G2 = find_f_g2(2024)

print(F2)
print(G2)

results2 = F2 + 3 - G

print(f"Happy {results2} Day!!!")