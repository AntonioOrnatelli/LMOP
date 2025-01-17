from abc import abstractmethod

from pulp import CPLEX_PY, LpMaximize, LpProblem, lpSum, LpVariable, LpInteger, value


class MOProblem:

    def __init__(self, n: int, x_bounds: tuple[float, float] | list[tuple[float, float]]) -> None:
        self.n = n
        self.set_variables = range(0, n)
        if isinstance(x_bounds, tuple):
            self.x_ub = x_bounds[1]
            self.x_lb = x_bounds[0]
        else:
            self.x_ub = [x_bounds[i][1] for i in self.set_variables]
            self.x_lb = [x_bounds[i][0] for i in self.set_variables]
        self.problem = LpProblem(self.problem_name, LpMaximize)
        self.x = LpVariable.dicts("x", self.set_variables, cat=LpInteger)
        self._f = []
        self._f_ub = []
        self._f_lb = []

    @abstractmethod
    def build_problem(self) -> None:
        pass

    def solve_as_single_objective(self, weights: list, mip_gap: float, print_log: bool=False) -> None:
        self._build_single_objective_function(weights)
        self.problem.solve(CPLEX_PY(gapRel=mip_gap, msg=print_log))

    @property
    def objective_functions(self) -> list:
        return self._f

    @property
    def variables(self) -> list:
        return [self.x[i] for i in self.set_variables]

    @property
    def variables_values(self) -> list:
        return [value(self.x[i]) for i in self.set_variables]

    @property
    def objective_function_upper_bounds(self) -> list:
        return self._f_ub

    @property
    def objective_function_lower_bounds(self) -> list:
        return self._f_lb

    def _build_single_objective_function(self, weights: list):
        self.problem += lpSum(
            [weights[i] * (self._f[i] - self._f_lb[i]) for i in self.set_variables]
        )

    @property
    def problem_name(self):
        return "Multi-Objective_Problem"