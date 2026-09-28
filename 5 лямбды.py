import math

m = 8.020823
v = 2.816756
q = 0.2

q_max = 2.0 / (1.0 + v * v)
print(f"Верхняя граница q: {q_max:.6f}")
if q >= q_max:
    raise ValueError("q должно быть строго меньше 2/(1+v^2)")

m1 = m
m2 = (1.0 + v * v) * m * m

A = q
B = -2.0 * q * m1
C = m1 * m1 - m2 * (1.0 - q) / 2.0

D = B * B - 4.0 * A * C
print(f"\nДискриминант D = {D:.6f}")
if D < 0:
    raise ValueError("Дискриминант отрицательный — система не имеет решения")

sqrtD = math.sqrt(D)
x1 = (-B + sqrtD) / (2.0 * A)
x2 = (-B - sqrtD) / (2.0 * A)
y1 = (m1 - q * x1) / (1 - q)
y2 = (m1 - q * x2) / (1 - q)

candidates = [(x1, y1), (x2, y2)]
valid = [(x, y) for (x, y) in candidates if x > 0 and y > 0]

if not valid:
    raise ValueError("Нет положительного решения")

x, y = valid[0]

lam1 = 1.0 / x
lam2 = 1.0 / y

print(f"\nРешение:")
print(f"  λ1 = {lam1:.6f}   (округлённо: {lam1:.3f})")
print(f"  λ2 = {lam2:.6f}   (округлённо: {lam2:.3f})")

# проверка
m_check  = q / lam1 + (1 - q) / lam2
m2_check = 2 * q / lam1**2 + 2 * (1 - q) / lam2**2
v_check  = math.sqrt(m2_check / m_check**2 - 1)

print(f"\nпроверка (обратная подстановка):")
print(f"  m  = {m_check:.6f}   (должно быть {m:.6f})")
print(f"  m2 = {m2_check:.6f}   (должно быть {m2:.6f})")
print(f"  v  = {v_check:.6f}   (должно быть {v:.6f})")

print(f"$ lambda_1 approx {lam1:.3f}, quad lambda_2 approx {lam2:.3f}. $")