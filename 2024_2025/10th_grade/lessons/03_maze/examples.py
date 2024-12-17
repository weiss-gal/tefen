maze1 = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0]
]

good_solution = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
# hitting wall
bad_solution_1 = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
# not starting at the beginning
bad_solution_2 = good_solution[1:]
# not reaching the end
bad_solution_3 = good_solution[:-1]
# diagonal move
bad_solution_3 = [(0, 0), (1, 1), (1, 2), (2, 2)]

# long good solution
good_solution_long = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 1), (1, 2), (2, 2)]

