import math

with open("generated.txt", "r", encoding="utf-8") as f:
    data = [float(line.strip()) for line in f if line.strip()]

N = len(data)

sizes = [10, 20, 50, 100, 200, 300]
T_P = {0.90: 1.643, 0.95: 1.960, 0.99: 2.576}

def calc_mean(sample):
    s = 0.0
    for x in sample:
        s += x
    return s / len(sample)

def calc_variance(sample, m):
    s = 0.0
    for x in sample:
        s += (x - m) ** 2
    return s / (len(sample) - 1)

def calc_std(sample, m):
    return math.sqrt(calc_variance(sample, m))

def conf_interval(sample, m, p):
    n = len(sample)
    return T_P[p] * calc_std(sample, m) / math.sqrt(n)

results = {}
for n in sizes:
    sample = data[:n]
    m = calc_mean(sample)
    d = calc_variance(sample, m)
    s = math.sqrt(d)
    cv = s / m
    results[n] = dict(m=m, d=d, s=s, cv=cv,
                      ci90=conf_interval(sample, m, 0.90),
                      ci95=conf_interval(sample, m, 0.95),
                      ci99=conf_interval(sample, m, 0.99))

ref = results[300]

def rel(v, r):
    return 0.0 if r == 0 else (v - r) / r * 100

def fmt(x):     return f"{x:.6f}"
def fmt_pct(x): return f"{x:+.4f}"
def fmt_ci(x):  return f"±{x:.4f}"

def row(title, key, formatter):
    vals = [results[n][key] for n in sizes]

    # строка с нужными значениями, отдельно 300
    vals_cells = ", ".join(f"[{formatter(v)}]" for v in vals[:-1])
    print(f"  table.cell(rowspan: 2)[{title}], [знач], {vals_cells}, table.cell(rowspan: 2)[{formatter(vals[-1])}],")

    # вторая строка, проценты от 300
    pct_cells = ", ".join(f"[{fmt_pct(rel(v, ref[key]))}]" for v in vals[:-1])
    print(f"  [%], {pct_cells},")
    print()

print("#table(")
print("  columns: 8,")
print("  table.cell(rowspan: 2)[характеристика], [], table.cell(colspan: 6)[количество случайных величин],")
print("  [], [10], [20], [50], [100], [200], [300],\n")

row("мат ож",       "m",    fmt)
row("дов инт",      "ci90", fmt_ci)
row("дов инт",      "ci95", fmt_ci)
row("дов инт",      "ci99", fmt_ci)
row("дисперсия",    "d",    fmt)
row("ско",          "s",    fmt)
row("к-т вариации", "cv",   fmt)

print(")")