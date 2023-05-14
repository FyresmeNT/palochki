import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( -2*np.pi, 2*np.pi, 3000)
y1 = 9/5*x**4-np.sin(10*x)
y2 = 2*x*np.sin(x)-np.cos(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

