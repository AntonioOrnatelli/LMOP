import numpy as np

def compute_weights(n, lb, ub, epsilon, k) -> tuple:
    lambda_ = []
    lambda_.append(1 / (ub[0] - lb[0]))
    for i in range(1, n):
        lambda_.append(lambda_[i - 1] * epsilon / (ub[i] - lb[i]))
    delta = k / (lambda_[n - 1] * epsilon)
    mip_gap = lambda_[n - 1] * epsilon * (ub[0] - lb[0]) / ub[0]
    weights = [delta*lambda_[i] for i in range(n)]
    return weights, mip_gap


def get_random_rotation(n) -> np.ndarray:
    T = np.random.rand(n, n)
    Q, R = np.linalg.qr(T)
    return Q

