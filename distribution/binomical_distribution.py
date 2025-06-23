import numpy as np
import matplotlib.pyplot as plt
from math import comb, floor, sqrt


def binomical_dist(n, p):
    x = np.arange(0, n + 1)
    pmf = np.array([comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in x])

    mean = n * p
    var = n * p * (1 - p)
    std = sqrt(var)

    plt.figure(figsize=(10, 6))
    plt.bar(x, pmf, color='skyblue', edgecolor='black')
    plt.title(f'Биномиальное распределение: n = {n}, p = {p}')
    plt.xlabel('k')
    plt.ylabel('P(X = k)')


    legend_text = (
        f"Математическое ожидание: {mean:.2f}\n"
        f"Дисперсия: {var:.2f}\n"
        f"СКО: {std:.2f}\n"
    )

    plt.legend([legend_text], loc='upper right')

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

