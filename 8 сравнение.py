import math
import matplotlib.pyplot as plt

# чтение данных
def read_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]

data = read_numbers("data.txt")          # заданная чп
gen  = read_numbers("generated.txt")     # сгенерированная чп

n = min(len(data), len(gen))
data = data[:n]
gen  = gen[:n]

# график значений
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(range(1, n + 1), data, linewidth=0.7, color="#1f77b4", label="заданная чп")
ax.plot(range(1, n + 1), gen,  linewidth=0.7, color="#d62728", alpha=0.7, label="сгенерированная чп")

ax.set_title("Сравнение заданной и сгенерированной последовательностей", fontsize=14)
ax.set_xlabel("Индекс", fontsize=12)
ax.set_ylabel("Значение", fontsize=12)
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
ax.legend()

plt.tight_layout()
plt.savefig("plot_compare_sequence.png", dpi=200)
plt.show()
print("Сохранено: plot_compare_sequence.png")

# гистограмма
# общий диапазон и одинаковые интервалы для обеих чп
x_min = min(min(data), min(gen))
x_max = max(max(data), max(gen))
k = 18
step = (x_max - x_min) / k
edges = [x_min + i * step for i in range(k + 1)]

def frequencies(series, edges):
    freq = [0] * (len(edges) - 1)
    for x in series:
        idx = int((x - x_min) / step)
        if idx >= len(freq):
            idx = len(freq) - 1
        freq[idx] += 1
    return freq

freq_data = frequencies(data, edges)
freq_gen  = frequencies(gen,  edges)

centers = [(edges[i] + edges[i+1]) / 2 for i in range(k)]
half_width = [(edges[i+1] - edges[i]) / 2 for i in range(k)]   # половина ширины

fig, ax = plt.subplots(figsize=(14, 6))

# столбики заданной чп, левая половина
ax.bar([c - hw/2 for c, hw in zip(centers, half_width)], freq_data,
       width=half_width, edgecolor="black", color="#1f77b4", label="заданная чп")

# столбики сгенерированной чп, правая половина
ax.bar([c + hw/2 for c, hw in zip(centers, half_width)], freq_gen,
       width=half_width, edgecolor="black", color="#d62728", alpha=0.8, label="сгенерированная чп")

ax.set_title("Сравнение гистограмм распределения частот", fontsize=14)
ax.set_xlabel("Интервалы значений", fontsize=12)
ax.set_ylabel("Частота", fontsize=12)
ax.grid(True, axis="y", linestyle="--", linewidth=0.5, alpha=0.7)
ax.legend()

ax.set_xticks(edges)
ax.set_xticklabels([f"{e:.2f}" for e in edges], rotation=45, ha="right", fontsize=8)

plt.tight_layout()
plt.savefig("plot_compare_histogram.png", dpi=200)
plt.show()
print("Сохранено: plot_compare_histogram.png")

# таблица для typst
def fmt(x):
    return f"{x:.4f}"

print("\n# ====== таблица интервалов и частот для typst ======\n")
print("#figure(")
print("  table(")
print("    columns: 4,")
print("    align: center,")
print("    stroke: 0.5pt,")
print("    inset: 4pt,")
print("    table.header([№], [Интервал], [Частота (зад.)], [Частота (сген.)]),")
for i in range(k):
    interval = f"{fmt(edges[i])} – {fmt(edges[i+1])}"
    print(f"    [{i+1}], [{interval}], [{freq_data[i]}], [{freq_gen[i]}],")
print("  ),")
print("  caption: [Сравнение частот заданной и сгенерированной ЧП],")
print(")")