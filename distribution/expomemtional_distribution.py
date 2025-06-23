import numpy as np
import matplotlib.pyplot as plt
from math import exp, sqrt

def exp_dist(lmbda):
    n_samples = 10000
    samples = np.random.exponential(scale=1 / lmbda, size=n_samples)

    x = np.linspace(0, np.percentile(samples, 99), 500)

    pdf = lmbda * np.exp(-(lmbda * x))
    cdf = 1 - np.exp(-(lmbda * x))

    mean = 1 / lmbda
    var = 1 / lmbda ** 2
    std_dev = sqrt(var)
    mode = 0
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    axs[0].hist(samples, bins=50, density=True, alpha=0.5, color='skyblue', label='Гистограмма выборки')
    axs[0].plot(x, pdf, 'r-', lw=2, label='Теоретическая PDF')
    axs[0].set_title('Показательное распределение: PDF')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Плотность')
    axs[0].grid(True, linestyle='--', alpha=0.5)

    legend_pdf = (
        f"Математическое ожидание: {mean:.2f}\n"
        f"Дисперсия: {var:.2f}\n"
        f"СКО: {std_dev:.2f}\n"
        f"Мода: {mode}"
    )
    axs[0].legend([legend_pdf], loc='upper right')

    axs[1].plot(x, cdf, 'g-', lw=2, label='Теоретическая CDF')
    axs[1].set_title('Показательное распределение: CDF')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('F(x)')
    axs[1].grid(True, linestyle='--', alpha=0.5)
    axs[1].legend(loc='lower right')

    plt.tight_layout()
    plt.show()

