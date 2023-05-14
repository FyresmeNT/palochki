from scipy.integrate import quad
import numpy as np

def integral (x):
    return 1/np.sqrt(6*x-x**2-8)

result, error = quad (integral, 2, 4)

print("Значение интеграла равно:", result)