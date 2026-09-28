def read_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]

data = read_numbers("data.txt")

# автокорреляция со сдвигом tau
def autocorr(series, tau):
    n = len(series)
    mean = sum(series) / n
    denom = sum((x - mean) ** 2 for x in series)
    num = sum((series[i] - mean) * (series[i + tau] - mean) for i in range(n - tau))
    return num / denom

max_lag = 10
acf = [autocorr(data, tau) for tau in range(1, max_lag + 1)]

print("Сдвиг\tКоэф. автокорреляции")
for tau, r in enumerate(acf, start=1):
    print(f"{tau}\t{r:+.6f}")

def fmt(x):
    return f"{x:+.4f}"

vals = ", ".join(f"[{fmt(v)}]" for v in acf)

print("\n# ====== таблица для typst (форма 3) ======\n")
print("#figure(")
print("  table(")
print("    columns: 11,")
print("    align: center,")
print("    stroke: 0.5pt,")
print("    inset: 4pt,")
print("    table.header(")
print("      [Сдвиг ЧП], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],")
print("    ),")
print(f"    [К-т АК для задан. ЧП], {vals},")
print("  ),")
print("  caption: [Форма 3. Коэффициенты автокорреляции],")
print(")")