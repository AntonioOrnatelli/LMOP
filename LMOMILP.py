from pulp import *
import time

from kite_problem import KiteProblem
from utils import compute_weights, get_random_rotation


print("***** Problem 1: the kite in 2D ****")
# Variables upper and lower bounds
x_ub = 200
x_lb = -200
# Weights computation parameters
epsilon = 0.1
k = 0.1
# Problem definition
kite_problem = KiteProblem((x_lb, x_ub), (x_lb, x_ub))
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
print("Seconds to compute weights: ", time.time() - start_time)
kite_problem.solve_as_single_objective(weights, mip_gap)
print("Total seconds to solve the problem: ", time.time() - start_time)

print("MIP_GAP: ", mip_gap)
print("Weights: ", [w for w in weights])
print("Optimal values: ", kite_problem.variables_values)

print("***** Problem 5: randomly rotated hypercube ****")
# Number of objectives and variables upper bounds
n = 200
ub = 100.2
lb = -100.2
# Weights computation parameters
epsilon = 7
k = 1
# Problem definition
hypercube_prob = LpProblem("randomly_rotated_hypercube", LpMaximize)
set_variables = range(0, n)
x = LpVariable.dicts("x", set_variables, cat=LpInteger)
Q = get_random_rotation(n)
# Constraints
for i in range(0, n):
    q_sum = lpSum(Q[i][j] * x[j] for j in set_variables)
    hypercube_prob += q_sum >= -1000
    hypercube_prob += q_sum <= 1000
    hypercube_prob += x[i] >= lb
    hypercube_prob += x[i] <= ub

start_time = time.time()
# Compute weights
weights, mip_gap = compute_weights(n, [lb] * n, [ub] * n, epsilon, k)
print("Seconds to compute weights: ", time.time() - start_time)
# Add the equivalent single-objective function to the problem
hypercube_prob += lpSum([weights[i] * (x[i] - lb) for i in set_variables])
hypercube_prob.solve(CPLEX_PY(gapRel=mip_gap))
print("Total seconds to solve the problem: ", time.time() - start_time)

print("MIP_GAP: ", mip_gap)
print("Weights: ", [w for w in weights])
print("Optimal values: ", [value(x[i]) for i in set_variables])
