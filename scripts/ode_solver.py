from typing import Callable, List


def solve_euler(ybisfunc: List[Callable], step: float, rang: float, init: List[float]):
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
