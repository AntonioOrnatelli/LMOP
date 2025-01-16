from pulp import *
import time

from utils import compute_weights, get_random_rotation


print("***** Problem 1: the kite in 2D ****")
# Variables upper and lower bounds
x_ub = 200
x_lb = -200
# Weights computation parameters
epsilon = 0.1
k = 0.1
# Problem definition
kite_problem = LpProblem("kite_problem", LpMaximize)
x1 = LpVariable("x1", cat=LpInteger)
x2 = LpVariable("x2", cat=LpInteger)
# Constraints
kite_problem += 2*x1 + x2 <= 120
kite_problem += 2*x1 + 3*x2 <= 212.5
kite_problem += 4*x1 + 3*x2 <= 270
kite_problem += x1 + 2*x2 >= 60
kite_problem += x1 >= x_lb
kite_problem += x1 <= x_ub
kite_problem += x2 >= x_lb
kite_problem += x2 <= x_ub
# Objective functions
f = [8*x1 + 12*x2, 14*x1 + 10*x2, x1 + x2]

start_time = time.time()
# Lists of cost functions upper and lower bounds
lb = []
ub = []
lb.append(8 * x_lb + 12 * x_lb)
ub.append(8 * x_ub + 12 * x_ub)
lb.append(14 * x_lb + 10 * x_lb)
ub.append(14 * x_ub + 10 * x_ub)
lb.append(x_lb + x_lb)
ub.append(x_ub + x_ub)
# Compute weights
weights, mip_gap = compute_weights(3, lb, ub, epsilon, k)
# Add the equivalent single-objective function to the problem
kite_problem += lpSum([weights[i] * (f[i] - lb[i]) for i in range(3)])
print("Seconds to compute weights: ", time.time() - start_time)
kite_problem.solve(CPLEX_PY(gapRel=mip_gap))
print("Total seconds to solve the problem: ", time.time() - start_time)

print("MIP_GAP: ", mip_gap)
print("Weights: ", [w for w in weights])
print("Optimal values: ", (value(x1), value(x2)))

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
