import time

from problems.kite_problem import KiteProblem
from problems.rotated_hypercube import RotatedHypercubeProblem
from utils import compute_weights, print_results

# Problem 1: Kite in 2D and 3 objectives
# Variables upper and lower bounds
x_ub = 200
x_lb = -200
# Weights computation parameters
epsilon = 0.1
k = 0.1
# Problem definition
kite_problem = KiteProblem(2, [(x_lb, x_ub), (x_lb, x_ub)])
kite_problem.build_problem()
start_time = time.time()
# Compute weights
weights, mip_gap = compute_weights(
    len(kite_problem.objective_functions),
    kite_problem.objective_function_lower_bounds,
    kite_problem.objective_function_upper_bounds,
    epsilon,
    k,
)
weights_time = time.time() - start_time
kite_problem.solve_as_single_objective(weights, mip_gap)
total_time = time.time() - start_time
print_results(kite_problem, weights, mip_gap, weights_time, total_time)


# Problem 2: Randomly rotated hypercube in 200D and 200 objectives
# Number of objectives and variables upper bounds
n = 200
ub = 100.2
lb = -100.2
# Weights computation parameters
epsilon = 7
k = 1
# Problem definition
hypercube_problem = RotatedHypercubeProblem(n, (lb, ub))
hypercube_problem.build_problem()
start_time = time.time()
# Compute weights
weights, mip_gap = compute_weights(n, [lb] * n, [ub] * n, epsilon, k)
weights_time = time.time() - start_time
hypercube_problem.solve_as_single_objective(weights, mip_gap)
total_time = time.time() - start_time
print_results(hypercube_problem, weights, mip_gap, weights_time, total_time)
