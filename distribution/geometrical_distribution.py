import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def geom_dist(p: float, k: int):
    x = np.arange(1, k + 1)
    pmf = (1 - p) ** (x - 1) * p

    mean = 1 / p
    var = (1 - p) / p**2
    std_dev = sqrt(var)
    mode = 1

    plt.figure(figsize=(10, 6))
    plt.bar(x, pmf, color='blue', edgecolor='black')

    plt.title(f'Геометрическое распределение (p = {p})')
    plt.xlabel('Количество испытаний до первого успеха (X)')
    plt.ylabel('P(X = k)')
    plt.xticks(x)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Легенда
    legend_text = (
        f"Математическое ожидание: {mean:.2f}\n"
        f"Дисперсия: {var:.2f}\n"
        f"СКО: {std_dev:.2f}\n"
        f"Мода: {mode}"
    )
    plt.legend([legend_text], loc='upper right')

    plt.tight_layout()
    plt.show()

