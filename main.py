import scipy.integrate as scpi
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, List

A = 0.001
g = 9.8


def funcy1bis(y: List[float], t):
    if y[0] >= 0:
        r = y[1]
        return y[1]
    return 0


def funcy2bis(y: List[float], t):
    A = 0.002
    g = 9.81
    return -y[1] ** 2 * A - g

def funcx1bis(x: List[float], t):
    return x[1]


def funcx2bis(x: List[float], t):
    A = 0.002
    r = -x[1] ** 2 * A
    return -x[1] ** 2 * A


def solveEuler(ybisfunc: List[Callable], step: float, rang: float, init: List[float]):
    t = 0
    y = init
    soly = []
    for i in ybisfunc:
        soly.append([])

    for i in range(len(soly)):
        soly[i].append(init[i])

    tvect = [0]
    index = 1
    while t < rang:
        last_sol = []
        for i in range(len(soly)):
            last_sol.append(soly[i][index - 1])
        for i in range(len(soly)):
            soly[i].append(soly[i][index - 1] + step * ybisfunc[i](last_sol, t))
        t += step
        tvect.append(t)
        index += 1
    return soly, tvect


time = np.linspace(0, 100, 1000)
farr = [funcy1bis, funcy2bis]
farrx = [funcx1bis, funcx2bis]
plt.figure()
label = []
for i in range(20):
    fi = 90/20 * i + 3
    label.append(fi.__str__())
    fi = fi * np.pi/180
    solutionx = solveEuler(farrx, 0.001, 15, [0, 100*np.cos(fi)])
    solution = solveEuler(farr, 0.001, 15, [0, 100 * np.sin(fi)])
    plt.plot(solutionx[0][0], solution[0][0])
plt.legend(label)
plt.xlim([0,700])
plt.ylim([0,300])
plt.show()
