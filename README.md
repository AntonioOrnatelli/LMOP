# Weighting Method for Non-Preemptive Multi-Objective Mathematical Programming

This repository contains the code supporting the paper *Weighting Method for Non-Preemptive Multi-Objective Mathematical Programming* by L. Ferro, G. Filaci, A. Manzini, A. Ornatelli. This code has been used to produce the results presented in the section *Numerical Results* of the paper.

The code includes a Python implementation of the weighting method (`problems/multi_objective_problem.py`) and a script (`main.py`) which can be used to apply it to two given families of Lexicographic Multi-Objective Problems: a kite in 2D with 3 objectives and a randomly rotated hypercube in 200D with 200 objectives.
The single-objective problems derived from the LMOPs are then solved using the free and publicly available community edition of the commercial solver *CPLEX*.

Since the aim of these experiments is to compare the performance of our novel method to the one by Cococcioni et al., 2020 [[1]](#references), the same problems described in that paper are reconstructed and solved here.

## Usage
### Prerequisites
The code has been tested and executed on Python 3.10.15 running on an Apple M3 Pro with a 12-core CPU (6 performance cores up to 4.06 GHz and 6 efficiency cores up to 2.8 GHz).
It may work on other versions of Python and produce comparable results on different hardware.

### Installation
Install the required packages by running:
```bash
pip install -r requirements.txt
```

### Running the Code
To run the code, simply execute the script `main.py:
```bash
python main.py
```

The script will run and print the timing and the results of the experiments on the two families of problems.

## References
[1] Cococcioni, M., Cudazzo, A., Pappalardo, M., and Sergeyev, Y. D. (2020). Solving the lexicographic multi-objective mixed-integer linear programming problem using branch-and-bound and grossone methodology. *Communications in Nonlinear Science and Numerical Simulation*, 84:105177.

## License
This code is released under the MIT License. See the [LICENSE](LICENSE) file for more information.