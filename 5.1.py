import matplotlib.pyplot as plt
import numpy as np


def f(t, у):
    return np.tan(t)/y**2

y0 = 1
t = np.linspace(-np.pi, np.pi, 3000)

y = 3*np.log(np.abs(np.cos(t))**(1/3))+1

# Нарисуйте решение
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Решение задачи Коши: y\' = tg(t)/y^2, y(0) = 1')
plt.show()