import math
import matplotlib.pyplot as plt

def read_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]

data = read_numbers("data.txt")
n = len(data)


k = 18
x_min = min(data)
x_max = max(data)
step = (x_max - x_min) / k
edges = [x_min + i * step for i in range(k + 1)]

freq = [0] * k
for x in data:
    idx = int((x - x_min) / step)
    if idx == k:      # крайнее значение в последний
        idx = k - 1
    freq[idx] += 1

print("№\tЛевая\tПравая\tЧастота")
for i in range(k):
    print(f"{i+1}\t{edges[i]:.4f}\t{edges[i+1]:.4f}\t{freq[i]}")

print(f"\nСумма частот: {sum(freq)} (должно быть {n})")

fig, ax = plt.subplots(figsize=(14, 6))

centers = [(edges[i] + edges[i+1]) / 2 for i in range(k)]
widths  = [edges[i+1] - edges[i] for i in range(k)]

ax.bar(centers, freq, width=widths, edgecolor="black", color="#4472C4")

ax.set_title("Гистограмма распределения частот", fontsize=14)
ax.set_xlabel("Интервалы значений", fontsize=12)
ax.set_ylabel("Частота", fontsize=12)
ax.grid(True, axis="y", linestyle="--", linewidth=0.5, alpha=0.7)

ax.set_xticks(edges)
ax.set_xticklabels([f"{e:.2f}" for e in edges], rotation=45, ha="right", fontsize=8)

plt.tight_layout()
plt.savefig("plot3_histogram.png", dpi=200)
plt.show()

print("\nСохранено: plot3_histogram.png")

def fmt(x):
    return f"{x:.3f}"

header_nums = ", ".join(f"[{i+1}]" for i in range(k))
left_edges  = ", ".join(f"[{fmt(edges[i])}]" for i in range(k))
right_edges = ", ".join(f"[{fmt(edges[i+1])}]" for i in range(k))
freq_vals   = ", ".join(f"[{freq[i]}]" for i in range(k))

print("\n# ====== таблица интервалов для typst ======\n")
print("#figure(")
print("  table(")
print(f"    columns: {k+1},")
print("    align: center,")
print("    stroke: 0.5pt,")
print("    inset: 3pt,")
print("    table.header(")
print(f"      [Интервалы], {header_nums},")
print("    ),")
print(f"    [Левая граница], {left_edges},")
print(f"    [Правая граница], {right_edges},")
print(f"    [Частота], {freq_vals},")
print("  ),")
print("  caption: [Таблица интервалов и частот],")
print(")")