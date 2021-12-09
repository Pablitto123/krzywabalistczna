
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, List
import scripts.ode_solver as ode_solver
A = 0.001
g = 9.8


def funcy1bis(y: List[float], t):
    if y[0] >= 0:
        r = y[1]
        return y[1]
    return 0


def funcy2bis(y: List[float], t):
    A = 0.001
    g = 9.81
    return (-y[1] ** 2 * A) - g if y[0]>0 else 0

def funcx1bis(x: List[float], t):
    return x[1]


def funcx2bis(x: List[float], t):
    A = 0.001
    r = -x[1] ** 2 * A
    return -x[1] ** 2 * A

def oscFunxbis1(x, t):
    return x[1]
def oscFunxbis2(x, t):
    return -x[0] - 0.7*x[1] + 10


farr = [funcy1bis, funcy2bis]
farrx = [funcx1bis, funcx2bis]
plt.figure()
# plt.subplot(1,2,1)
# label = []
# speed =100
# maxy = 0
# maxx = 0
# for i in range(6):
#     fi = 90/6 * i
#     label.append(fi.__str__())
#     fi = fi * np.pi/180
#     solutionx = ode_solver.solve_euler(farrx, 0.0001, 30, [0, speed*np.cos(fi)])
#     solution = ode_solver.solve_euler(farr, 0.0001, 30, [0, speed * np.sin(fi)])
#     maxy = max(max(solution[0][0]), maxy)
#     plt.subplot(1, 2, 1)
#     plt.plot(solutionx[0][0], solution[0][0])
#     plt.subplot(1, 2, 2)
#     plt.plot(solutionx[1], solutionx[0][1])
#     for i in range(len(solutionx[0][0])):
#         if solution[0][0][i] > 0:
#             maxx = max(maxx, solutionx[0][0][i])
# plt.legend(label)
# plt.subplot(1, 2, 1)
# plt.xlim([0,maxx +100])
# plt.ylim([0,maxy+50])
plt.figure()
foscarr = [oscFunxbis1, oscFunxbis2]
solosc = ode_solver.solve_euler(foscarr, 0.0001, 30, [0, 5])
plt.plot(solosc[1], solosc[0][1], solosc[1], solosc[0][0])
plt.grid("on")
plt.show()