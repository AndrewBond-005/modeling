import math

# чтение данных
def read_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]

data = read_numbers("data.txt")          # заданная чп
gen  = read_numbers("generated.txt")     # сгенерированная чп

n = min(len(data), len(gen))
data = data[:n]
gen  = gen[:n]

# средние
def calc_mean(sample):
    return sum(sample) / len(sample)

mx = calc_mean(data)
my = calc_mean(gen)

# корреляция пиерсона
# r = sum((xi-x̄)(yi-ȳ)) / sqrt(sum((xi-x̄)^2) * sum((yi-ȳ)^2))
num  = 0.0
dx2  = 0.0
dy2  = 0.0
for i in range(n):
    dx = data[i] - mx
    dy = gen[i]  - my
    num += dx * dy
    dx2 += dx * dx
    dy2 += dy * dy

r = num / math.sqrt(dx2 * dy2)

# вывод
print(f"n = {n}")
print(f"среднее заданной чп        x̄ = {mx:.6f}")
print(f"среднее сгенерированной чп ȳ = {my:.6f}")
print()
print(f"числитель          sum(x-x̄)(y-ȳ) = {num:+.6f}")
print(f"sum(x-x̄)^2                     = {dx2:.6f}")
print(f"sum(y-ȳ)^2                     = {dy2:.6f}")
print(f"sqrt(sum(x-x̄)^2 * sum(y-ȳ)^2)  = {math.sqrt(dx2 * dy2):.6f}")
print()
print(f"коэффициент корреляции  r  = {r:+.6f}")
print(f"                        |r| = {abs(r):.6f}")

# для typst
print()
print("# ====== для typst ======")
print(f"$ r = {r:+.4f}, quad |r| = {abs(r):.4f}. $")