import matplotlib.pyplot as plt

# чтение данных
with open("data.txt", "r", encoding="utf-8") as f:
    data = [float(line.strip()) for line in f if line.strip()]

n = len(data)
x = list(range(1, n + 1))

# график
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(x, data, linewidth=0.7, color="#1f77b4")

ax.set_title("График числовой последовательности", fontsize=14)
ax.set_xlabel("Индекс", fontsize=12)
ax.set_ylabel("Значение", fontsize=12)
ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.savefig("plot1_sequence.png", dpi=200)
plt.show()

print("Сохранено: plot1_sequence.png")