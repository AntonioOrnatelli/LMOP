import numpy as np


def compute_weights(n: int, lb: list, ub: list, epsilon: list[float] | float, k: float, s: float = 1.0) -> tuple:
    """ Algorithm to compute the weights for the single objective problem. """
    if isinstance(epsilon, float):
        epsilon = [epsilon] * n
    lambda_ = []
    lambda_.append(1 / (ub[0] - lb[0]))
    for i in range(1, n):
        lambda_.append(lambda_[i - 1] * epsilon[i - 1] / (ub[i] - lb[i]) / (1 + (epsilon[i] / (ub[i] - lb[i]))))
    delta = k / (lambda_[n - 1] * epsilon[-1])
    mip_gap = s * lambda_[n - 1] * epsilon[-1]
    weights = [delta*lambda_[i] for i in range(n)]
    return weights, mip_gap

def get_random_rotation(n) -> np.ndarray:
    T = np.random.rand(n, n)
    Q, R = np.linalg.qr(T)
    return Q

def print_results(problem, weights, mip_gap, weights_time, total_time):
    print("Problem: ", problem.problem.name)

    print("Single objective weights computation time: ", weights_time, "seconds")
    print("Total time to solve the problem: ", total_time, "seconds")

    print("MIP_GAP: ", mip_gap)
    print("Weights: ", [w for w in weights])
    print("Optimal values: ", problem.variables_values)
    print("\n")