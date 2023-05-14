import matplotlib.pyplot as plt
import numpy as np

def f(t, y):
    return np.tan(t)/y**2

def RK4_step(f, t, y, h):
    k1 = h*f(t, y)
    k2 = h*f(t + 0.5*h, y + 0.5*k1)
    k3 = h*f(t + 0.5*h, y + 0.5*k2)
    k4 = h*f(t + h, y + k3)
    return y + (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0

t0 = 0.0
y0 = 1.0
t_end = 1.0
h = 0.01

t_values   = np.arange(t0, t_end+h, h)
y_values   = np.zeros_like (t_values)
y_values[0] = y0

for i in range (1, len(t_values)):
    y_values[i] = RK4_step(f, t_values[i-1], y_values[i-1], h)

plt.plot (t_values, y_values)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Решение задачи Коши')
plt.show()