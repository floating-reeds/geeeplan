from pysat.solvers import Solver
from pysat.card import CardEnc
'''
def encode_sat(grid_rows, grid_cols, shapes, adjacency_constraints):
    solver = Solver(name='g3')
    variables = {}

    var_count = 1
    for s, shape in enumerate(shapes):
        for r in range(grid_rows):
            for c in range(grid_cols):
                variables[(r, c, s)] = var_count
                var_count += 1

    for r in range(grid_rows):
        for c in range(grid_cols):
            covering_shapes = []
            for s, shape in enumerate(shapes):
                if all(0 <= r + dr < grid_rows and 0 <= c + dc < grid_cols for dr, dc in shape):
                    covering_shapes.append(variables[(r, c, s)])

            if covering_shapes:
                solver.add_clause(CardEnc.atmost(covering_shapes, 1, encoding=0)) 

    for (s1, s2) in adjacency_constraints:
        adjacency_clauses = []
        for r1 in range(grid_rows):
            for c1 in range(grid_cols):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
                    r2, c2 = r1 + dr, c1 + dc
                    if 0 <= r2 < grid_rows and 0 <= c2 < grid_cols:
                        if (r1, c1, s1) in variables and (r2, c2, s2) in variables:
                            adjacency_clauses.append([-variables[(r1, c1, s1)], variables[(r2, c2, s2)]])

        for clause in adjacency_clauses:
            solver.add_clause(clause)

    if solver.solve():
        model = solver.get_model()
        solution = {(r, c, s) for (r, c, s), v in variables.items() if v in model}
        return solution
    else:
        return None

shapes = [
    [(0, 0), (0, 1), (1, 0), (1, 1)], 
    [(0, 0), (0, 1), (0, 2)], 
]
adjacency_constraints = [(0, 1)] 
solution = encode_sat(5, 5, shapes, adjacency_constraints)

if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
'''