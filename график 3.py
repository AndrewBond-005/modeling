import math
import matplotlib.pyplot as plt

# параметры (из этапа 5)
q       = 0.2
lambda1 = 0.026392   # медленная компонента
lambda2 = 1.806937   # быстрая компонента

# чтение данных
def read_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]

data = read_numbers("data.txt")
n = len(data)

# гистограмма
k = 18
x_min = min(data)
x_max = max(data)
step = (x_max - x_min) / k
edges = [x_min + i * step for i in range(k + 1)]

freq = [0] * k
for x in data:
    idx = int((x - x_min) / step)
    if idx >= k:
        idx = k - 1
    freq[idx] += 1

# нормируем частоты: плотность = частота / (n * ширина интервала)
width = edges[1] - edges[0]
density_emp = [f / (n * width) for f in freq]

centers = [(edges[i] + edges[i+1]) / 2 for i in range(k)]

# теоретическая плотность
def hyperexp_pdf(x, q, l1, l2):
    return q * l1 * math.exp(-l1 * x) + (1 - q) * l2 * math.exp(-l2 * x)

# сетка x для плотности (от 0 до x_max)
n_plot = 500
x_grid = [x_max * i / n_plot for i in range(n_plot + 1)]
y_theor = [hyperexp_pdf(x, q, lambda1, lambda2) for x in x_grid]

# график
fig, ax = plt.subplots(figsize=(14, 6))

# гистограмма, эмпирическая плотность
ax.bar(centers, density_emp, width=width,
       edgecolor="black", color="#4472C4", alpha=0.7,
       label="гистограмма (заданная чп)")

# теоретическая плотность
ax.plot(x_grid, y_theor, color="#d62728", linewidth=2,
         label="плотность гиперэкспоненциального закона")

ax.set_title("Сравнение плотности распределения с гистограммой частот", fontsize=14)
ax.set_xlabel("Значение", fontsize=12)
ax.set_ylabel("Плотность вероятности", fontsize=12)
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
ax.legend()

plt.tight_layout()
plt.savefig("plot_density_over_hist.png", dpi=200)
plt.show()

print("сохранено: plot_density_over_hist.png")