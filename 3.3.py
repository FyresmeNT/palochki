import matplotlib.pyplot as plt
import numpy as np


x = np.linspace( -2*np.pi, 2*np.pi, 3000)
y1 = np.exp(x)
y2 = 2*(1-x)**2
plt.plot(x,y1)
plt.plot(x,y2)

idx = np.argwhere(np.diff(np.sign(y1 - y2))).flatten()
plt.plot(x[idx], y1[idx], 'ro')
plt.show()

print("Решение уравнения: ")
print("x =", x[idx])
print("y =", y1[idx])

x1 = np.linspace(-2*np.pi, 2*np.pi, 3000)
y3 = 2*np.log(x1)**2 - np.log(x1)
y4 = 1+x1-x1
# Построить график функции
plt.plot (x1, y3)
plt.plot (x1, y4)

idx = np.argwhere(np.diff(np.sign(y3 - y4))).flatten()
plt.plot(x1[idx], y3[idx], 'ro')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Решение неравенства: 2ln(x)^2 - ln(x) < 1')

# Показать сюжет
plt.show()

print("Решение неравенства: ")
print("x =", x1[idx])
print("y =", y3[idx])


