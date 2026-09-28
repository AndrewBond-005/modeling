import math
import random

# параметры (из этапа 5)
q       = 0.2
lambda1 = 0.026392   # медленная компонента
lambda2 = 1.806937   # быстрая компонента

t1 = 1.0 / lambda1
t2 = 1.0 / lambda2

n    = 300
seed = 42            # для воспроизводимости; убери если нужна другая последовательность

# генерация
random.seed(seed)

generated = []
for _ in range(n):
    r1 = random.random()
    r2 = random.random()
    t  = t1 if r1 < q else t2
    x  = t * (-math.log(1.0 - r2))
    generated.append(x)

# сохранение
with open("generated.txt", "w", encoding="utf-8") as f:
    for x in generated:
        f.write(f"{x:.6f}\n")

# отчет
print(f"Сгенерировано {n} значений")
print(f"параметры:")
print(f"  q  = {q}")
print(f"  λ1 = {lambda1}")
print(f"  λ2 = {lambda2}")
print(f"  t1 = 1/λ1 = {t1:.4f}")
print(f"  t2 = 1/λ2 = {t2:.4f}")
print(f"сохранено в файл: generated.txt")
print()
print("первые 10 значений:")
for x in generated[:10]:
    print(f"  {x:.6f}")