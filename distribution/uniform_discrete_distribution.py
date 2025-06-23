import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def uniform_dist(a, b):
    x = np.arange(a, b + 1)
    pdf = 1 / (b - a + 1)

    mean = (a + b) / 2
    var = ((b - a + 1) ** 2) / 12
    std_dev = sqrt(var)
    mo = "все значения"

    plt.figure(figsize=(10, 6))
    plt.bar(x, pdf, color='blue', edgecolor='black')

    plt.title(f"Равномерное дискретное распределение от {a} до {b}")
    plt.xlabel('Значение X')
    plt.ylabel("P(X) = x")
    plt.xticks(x)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)

    legend_text = (
        
        f"Математическое ожидание: {mean:.2f}\n"
        f"Дисперсия: {var:.2f}\n"
        f"СКО: {std_dev:.2f}\n"
        f"Мода: {mo}")

    plt.legend([legend_text], loc='upper right')


    plt.tight_layout()
    plt.show()

