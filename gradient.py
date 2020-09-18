import numpy as np
from util import *
import sys
# from draw import draw_lambda
from refractory import refractory


eps = 1e-4
epoch = 10000  # 最大迭代次数
size = 200  # 参与估计的时间序列长度


def time_exp(time, beta):
    """"
    :return:
        a[i][j] = exp(-beta(t_i-t_j))
        b[i][j] = exp(-beta(t_i-t_j))*(t_i-t_j)
        c[i][j] = exp(-beta(t_i-t_j))*(t_i-t_j)*(t_i-t_j)
    """
    n = len(time)
    aa = [[0 for _ in range(n)] for _ in range(n)]
    bb = [[0 for _ in range(n)] for _ in range(n)]
    cc = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            aa[i][j] = np.exp(-beta * (time[i] - time[j]))
            bb[i][j] = (time[i] - time[j]) * aa[i][j]
            cc[i][j] = (time[i] - time[j]) * bb[i][j]
    return aa, bb, cc


def get_sum(xx, i):
    """
    :return:
        X(i) = sum_{j<i} xx[i][j]
    """
    return sum(xx[i][:i])


# Likelihood function
def objective_func(p, aa, tn, n):
    alpha = p[0]
    beta = p[1]
    mu = p[2]
    f = -mu * tn
    for i in range(n):
        A = get_sum(aa, i)
        f += alpha / beta * (aa[n - 1][i] - 1) + np.log(mu + alpha * A)
    return f


def gd(n, p, aa, bb, tn):
    alpha = p[0]
    beta = p[1]
    mu = p[2]
    grad_alpha = 0
    grad_beta = 0
    grad_mu = 0
    for i in range(n):
        A = get_sum(aa, i)
        B = get_sum(bb, i)
        den = mu + alpha * A
        grad_alpha += 1 / beta * (aa[n - 1][i] - 1) + A / den
        grad_beta += -alpha / beta * (bb[n - 1][i] + 1 / beta * (aa[n - 1][i] - 1)) - alpha * B / den
        grad_mu += 1 / den
    grad_mu -= tn
    return np.array([grad_alpha, grad_beta, grad_mu])


def gradient_descent(p, lr, time):
    aa, bb, cc = time_exp(time, p[1])
    grad = gd(len(time), p, aa, bb, time[-1])
    new_p = p + grad * lr
    aa_, _, _ = time_exp(time, new_p[1])
    f = objective_func(new_p, aa_, time[-1], len(time))
    return new_p, f, grad


def mle(time):
    para = np.array([10.0, 20.0, 2.0])  # alpha, beta, mu
    lr = 0.1
    obj = -sys.maxsize
    for i in range(epoch):
        new_para, new_obj, grad = gradient_descent(para, lr, time)
        # para = new_para
        # obj = new_obj

        if new_obj < obj:
            lr /= 2
        else:
            para = new_para
            obj = new_obj

        if i % 100 == 0:
            print('Iter:', str(i), ' Parameter:', para, ' Gradient:', grad, ' likelihood:', obj, 'lr:', lr)
        if np.linalg.norm(grad) < eps:
            print('Finish iterating! Iteration times: ', i)
            break
    print(para, obj / len(time))
    # draw_lambda(para, time)


if __name__ == '__main__':
    # arrivals, channels = read_data('./data/simulation_2020.txt')
    # arrivals = get_channel(arrivals, 2020, channels)
    arrivals, channels = read_data('./data/1-1-4.spk.txt')
    arrivals = get_channel(arrivals, 18, channels)
    # arrivals, channels = read_data('./data/2-1-3.spk.txt')
    # arrivals = get_channel(arrivals, 11, channels)
    arrivals = arrivals[:size]
    print(arrivals)
    arrivals = refractory(arrivals, gamma=0.2)
    mle(arrivals)
