import numpy as np
import matplotlib.pyplot as plt
from math import pi, exp, sqrt

def normal_dist(mu: int, sigma: int):
    x = np.linspace(mu - 4*sigma, mu + 4 * sigma, 500)
    pdf  = (1 / (sqrt(2 * pi) * sigma)) * np.exp(-(((x - mu) ** 2) / (2 * sigma ** 2)))

    mean = mu
    var = sigma ** 2
    std_dev = sigma
    mo = mu

    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, color='blue', lw=2)
    plt.title(f'Нормальное распределение (μ = {mu}, σ = {sigma})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True, linestyle='--', alpha=0.5)

    legend_text = (
        f"Математичское ожидание {mean}",
        f"Дисперсия {var}",
        f"СКО {std_dev}",
        f"Мода {mo}"
    )

    plt.legend([legend_text], loc='upper right')
    plt.tight_layout()
    plt.show()

