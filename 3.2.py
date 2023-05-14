import numpy as np

m = float(input("Введите значение переменной m: "))
n = float(input("Введите значение переменной n: "))
while m==2*n:
    print("Неверные значения. Попробуйте заново")
    m = int(input("Введите значение переменной m: "))
    n = int(input("Введите значение переменной n: "))

A = np.linalg.inv(np.array([[m, -n],[2, -1]]))
B = np.transpose(np.array([(m-n)**2, 1]))
print("X= ", np.matmul(A,B))