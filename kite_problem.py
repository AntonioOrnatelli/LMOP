from pulp import CPLEX_PY, LpMaximize, LpProblem, lpSum, LpVariable, LpInteger, value


class KiteProblem:

    def __init__(self, x1_bounds: tuple, x2_bounds: tuple) -> None:
        self.x1_ub = x1_bounds[1]
        self.x1_lb = x1_bounds[0]
        self.x2_ub = x2_bounds[1]
        self.x2_lb = x2_bounds[0]
        self.problem = LpProblem("kite_problem", LpMaximize)
        self.x1 = LpVariable("x1", cat=LpInteger)
        self.x2 = LpVariable("x2", cat=LpInteger)

    def build_problem(self) -> None:
        self.problem += 2 * self.x1 + self.x2 <= 120
        self.problem += 2 * self.x1 + 3 * self.x2 <= 212.5
        self.problem += 4 * self.x1 + 3 * self.x2 <= 270
        self.problem += self.x1 + 2 * self.x2 >= 60
        self.problem += self.x1 >= self.x1_lb
        self.problem += self.x1 <= self.x1_ub
        self.problem += self.x2 >= self.x2_lb
        self.problem += self.x2 <= self.x2_ub

    def solve_as_single_objective(self, weights: list, mip_gap: float, print_log: bool=False) -> None:
        self._build_single_objective_function(weights)
        self.problem.solve(CPLEX_PY(gapRel=mip_gap, msg=print_log))

    @property
    def objective_functions(self) -> list:
        return [8*self.x1 + 12*self.x2, 14*self.x1 + 10*self.x2, self.x1 + self.x2]

    @property
    def variables(self) -> list:
        return [self.x1, self.x2]

    @property
    def variables_values(self) -> list:
        return [value(self.x1), value(self.x2)]

    @property
    def objective_function_upper_bounds(self) -> list:
        return [8*self.x1_ub + 12*self.x1_ub, 14*self.x1_ub + 10*self.x1_ub, self.x1_ub + self.x1_ub]

    @property
    def objective_function_lower_bounds(self) -> list:
        return [8*self.x1_lb + 12*self.x1_lb, 14*self.x1_lb + 10*self.x1_lb, self.x1_lb + self.x1_lb]

    def _build_single_objective_function(self, weights: list):
        self.problem += lpSum(
            [
                weights[i] * (self.objective_functions[i] - self.objective_function_lower_bounds[i])
                for i in range(len(self.objective_functions))
            ]
        )
