import matplotlib.pyplot as plt


def read_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]


gen = read_numbers("generated.txt")
n = len(gen)

def autocorr(series, tau):
    n = len(series)
    mean = sum(series) / n
    denom = sum((x - mean) ** 2 for x in series)
    num = sum((series[i] - mean) * (series[i + tau] - mean) for i in range(n - tau))
    return num / denom

max_lag = 10
acf = [autocorr(gen, tau) for tau in range(1, max_lag + 1)]

print("Сдвиг\tКоэф. автокорреляции")
for tau, r in enumerate(acf, start=1):
    print(f"{tau}\t{r:+.6f}")

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(range(1, max_lag + 1), acf, marker="o", linewidth=1.5, color="#1f77b4")
ax.axhline(0, color="black", linewidth=0.8)

ax.set_title("Автокорреляционный анализ сгенерированной чп", fontsize=14)
ax.set_xlabel("Сдвиг", fontsize=12)
ax.set_ylabel("Коэффициент автокорреляции", fontsize=12)
ax.set_xticks(range(1, max_lag + 1))
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.savefig("plot_autocorr_gen.png", dpi=200)
plt.show()

print("\nсохранено: plot_autocorr_gen.png")


def fmt(x):
    return f"{x:+.4f}"

vals = ", ".join(f"[{fmt(v)}]" for v in acf)

print("\n# ====== форма 3 для typst (сгенерированная чп) ======\n")
print("#figure(")
print("  table(")
print("    columns: 11,")
print("    align: center,")
print("    stroke: 0.5pt,")
print("    inset: 1pt,")
print("    table.header(")
print("      [Сдвиг ЧП], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],")
print("    ),")
print(f"    [К-т АК для сгенерир. ЧП], {vals},")
print("  ),")
print("  caption: [Форма 3. Коэффициенты автокорреляции сгенерированной ЧП],")
print(")")
