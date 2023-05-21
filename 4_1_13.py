import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Определение функции
def f(x):
    return x / 3 + np.arctan(x)
    

# 1. Область определения функции f(x)
# Функция f(x) определена для всех действительных значений x, поэтому нет ограничений на область определения.

# 2. Непрерывность функции f(x) и точки разрыва 1 и 2 рода
# Функция f(x) является непрерывной на всей области определения, поэтому нет точек разрыва.

# 3. Асимптоты
# Найдем вертикальные и наклонные асимптоты

# Вертикальные асимптоты:
# Функция f(x) не имеет вертикальных асимптот, так как не существует точек, в которых функция стремится к бесконечности.

# Наклонные асимптоты:
# Поведение функции на бесконечности характеризуется наклонными асимптотами, если они есть.
# Уравнение наклонной асимптоты имеет вид y = kx + b, где k = lim f(x) / x при x стремящемся к бесконечности, b = lim (f(x) - kx) при x стремящемся к бесконечности.

# Найдем коэффициенты наклонных асимптот
x = np.linspace(-10, 10, 1000)
y = f(x)

def k_b():
    x = sp.symbols('x')

    # Определение функции
    f = (x/3 + sp.atan(x))

    # Вычисление предела k
    limit_k = sp.limit(f / x, x, sp.oo)

    # Вычисление предела b
    limit_b = sp.limit(f - limit_k * x, x, sp.oo)

    print(limit_k, limit_b)
    return (limit_k, limit_b)

k, b = k_b()


# 4. Экстремумы
# Найдем координаты экстремумов функции f(x)
derivative = np.gradient(y)
extrema_indices = np.where(np.diff(np.sign(derivative)))[0]
extrema_x = x[extrema_indices]
extrema_y = y[extrema_indices]
print(f"Экстремумы: x = {extrema_x} y = {extrema_y}")


# 5. Построение графика функции f(x)
plt.plot(x, y, label='f(x) = x/3 + arctan(x)')
plt.plot(x, k * x + b, linestyle='dashed', color='red', label='Наклонная асимптота')

# Настройка осей и заголовка
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции f(x)')

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()
