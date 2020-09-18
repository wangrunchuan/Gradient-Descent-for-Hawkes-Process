import random
import numpy as np

eps = 1e-6


def iter_u(U, alpha, beta, mu, tk, S):
    u_prev = tk - np.log(U) / mu
    while True:
        f = np.log(U) + mu * (u_prev - tk) + alpha / beta * S * (1 - np.exp(-beta * (u_prev - tk)))
        f_diff = mu + alpha * S * np.exp(-beta * (u_prev - tk))
        u_next = u_prev - f / f_diff
        if abs(u_prev - u_next) < eps:
            break
        u_prev = u_next
    return 0.5 * (u_prev + u_next)


def simulate(alpha, beta, mu, n):
    times = []
    S = 1.0
    t1 = -np.log(random.random()) / mu
    times.append(t1)
    for i in range(n):
        U = random.random()
        t = iter_u(U, alpha, beta, mu, times[-1], S)
        times.append(t)
        S = np.exp(-beta * (t - times[-2])) * S + 1
        print(S)
    print(times)
    return times


if __name__ == '__main__':
    alpha = 4.0
    beta = 5.0
    mu = 2.0
    arrivals = simulate(alpha, beta, mu, 1000)
    # channel = random.randint(1000, 2000)
    channel = 2020
    file = './data/simulation_' + str(channel) + '.txt'
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(alpha) + ' ' + str(beta) + ' ' + str(mu) + '\n')
        for time in arrivals:
            f.write(str(time) + ' ' + str(channel) + '\n')
