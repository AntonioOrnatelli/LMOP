from problems.multi_objective_problem import MOProblem


class KiteProblem(MOProblem):
    PROBLEM_NAME = "kite_problem"

    def __init__(self, n: int,  x_bounds: list[tuple[float, float]]) -> None:
        super().__init__(n, x_bounds)
        self._f = [8*self.x[0] + 12*self.x[1], 14*self.x[0] + 10*self.x[1], self.x[0] + self.x[1]]
        self._f_ub = [8*self.x_ub[0] + 12*self.x_ub[1], 14*self.x_ub[0] + 10*self.x_ub[1], self.x_ub[0] + self.x_ub[1]]
        self._f_lb = [8*self.x_lb[0] + 12*self.x_lb[1], 14*self.x_lb[0] + 10*self.x_lb[1], self.x_lb[0] + self.x_lb[1]]

    def build_problem(self) -> None:
        self.problem += 2 * self.x[0] + self.x[1] <= 120
        self.problem += 2 * self.x[0] + 3 * self.x[1] <= 212.5
        self.problem += 4 * self.x[0] + 3 * self.x[1] <= 270
        self.problem += self.x[0] + 2 * self.x[1] >= 60
        self.problem += self.x[0] >= self.x_lb[0]
        self.problem += self.x[0] <= self.x_ub[0]
        self.problem += self.x[1] >= self.x_lb[1]
        self.problem += self.x[1] <= self.x_ub[1]

    @property
    def problem_name(self):
        return "Kite_Problem"