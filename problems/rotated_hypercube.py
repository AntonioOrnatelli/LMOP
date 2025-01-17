from pulp import lpSum

from problems.multi_objective_problem import MOProblem
from utils import get_random_rotation


class RotatedHypercubeProblem(MOProblem):
    PROBLEM_NAME = "rotated_hypercube_problem"

    def __init__(self, n: int, x_bounds: tuple[float, float]) -> None:
        super().__init__(n, x_bounds)
        self._f = [self.x[i] for i in self.set_variables]
        self._f_ub = [self.x_ub] * self.n
        self._f_lb = [self.x_lb] * self.n

    def build_problem(self) -> None:
        Q = get_random_rotation(self.n)
        # Constraints
        for i in range(0, self.n):
            q_sum = lpSum(Q[i][j] * self.x[j] for j in self.set_variables)
            self.problem += q_sum >= -1000
            self.problem += q_sum <= 1000
            self.problem += self.x[i] >= self.x_lb
            self.problem += self.x[i] <= self.x_ub

    @property
    def problem_name(self):
        return "Rotated_Hypercube_Problem"
