import numpy as np
import matplotlib.pyplot as plt
from math import exp, sqrt, factorial, floor

def poisson_dist(lmbd, k):
    x = np.arange(0, k + 1)
    pmf = np.array([(exp(-lmbd) * lmbd ** i) / factorial(i) for i in x])

    mean = lmbd
    var = lmbd
    std_dev = sqrt(var)
    mode = floor(lmbd) if lmbd != int(lmbd) else [lmbd - 1, lmbd]

    plt.figure(figsize=(10, 6))
    plt.bar(x, pmf, color='orchid', edgecolor='black')

    plt.title(f'Распределение Пуассона (λ = {lmbd})')
    plt.xlabel('k')
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

