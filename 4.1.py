import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1 - np.exp(x))

x = np.linspace (-10, 10, 1000)
y = np.exp(x)

# Проверить непрерывность и найти любые точки разрыва
if np.all (np.isfinite (y)):
    print("Функция непрерывна в своей области определения.")
else:
    print("Функция разрывна в следующих точках:", x[np.logical_not(np.isfinite(y))])

# Найдите вертикальную асимптоту(ы)
if np.any(np.isinf(y)):
    x_asymptote = x[np.isinf(y)][0] # предполагается, что только одна вертикальная асимптота
    print("Функция имеет вертикальную асимптоту в точке x =", x_asymptote)
else:
    print("У функции нет вертикальных асимптот.")

# Найдите любые максимумы и минимумы
diff = np.diff(y) / np.diff(x)
crit_points = x[np.where((out[:-1] * diff[1:]) < 0)[0] + 1]
if len(crit_points) == 0:
    print("Функция не имеет ни максимума, ни минимума.")
else:
    for c in crit_points:
        print("Функция имеет a", "максимум" if deriv[np.where(x == c)[0][0]] < 0 else "минимум", "at x =", c)

# Постройте функцию и асимптоты
plt.plot (х, у, label = 'f (х)')
if np.isinf(y).any():
    plt.axvline(x_asymptote, color='r', linestyle='--', label='Вертикальная асимптота')
plt.legend()
plt.xlabel('x')
plt.ylabel('у')
plt.show()