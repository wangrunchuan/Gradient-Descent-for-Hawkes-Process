import matplotlib.pyplot as plt
from util import *
import numpy as np


def draw_point(time, draw_channel, channels):
    x = get_channel(time, chosen_ch=draw_channel, channels=channels)
    y = [draw_channel for _ in range(len(x))]
    plt.scatter(x, y, marker='.', s=1)
    # plt.xlim(-20, 20)
    # plt.ylim(-1, 1)
    plt.show()


def lambda_t(arrivals, t, para):
    alpha = para[0]
    beta = para[1]
    mu = para[2]
    i = 0
    y = mu
    while arrivals[i] < t:
        y += alpha * np.exp(-beta * (t - arrivals[i]))
        i += 1
    return y


def draw_lambda(para, arrivals):
    print(arrivals)
    lam = []
    now = 0
    time = np.linspace(0, arrivals[-1], 100 * len(arrivals))
    x = []
    for j, t in enumerate(time):
        y = lambda_t(arrivals, t, para)
        lam.append(y)
        x.append(t)
        if time[j] < arrivals[now] < time[j + 1]:
            y = lambda_t(arrivals, t, para)
            lam.append(y)
            x.append(arrivals[now])
            now += 1
    tt = [0 for _ in range(len(arrivals))]
    plt.plot(x, lam, color='b', linewidth=0.5)
    plt.scatter(arrivals, tt, marker='.', s=1, color='r')
    plt.xlabel('t')
    plt.ylabel('λ')
    plt.savefig('./pic/18_small.jpg')
    plt.show()


# """
p = [-8.45469533, 9.51781679, 15.75711289]
arrivals, channels = read_data('./data/1-1-4.spk.txt')
arrivals = get_channel(arrivals, 18, channels)
arrivals = arrivals[:10]
"""

p = [3.58377323, 5.19868076, 2.17332204]
arrivals, channels = read_data('./data/simulation_2020.txt')
arrivals = get_channel(arrivals, 2020, channels)
arrivals = arrivals[:200]
"""
draw_lambda(p, arrivals)
