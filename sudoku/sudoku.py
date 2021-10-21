from constraint import Problem, BacktrackingSolver

problem = Problem(BacktrackingSolver())
problem.addVariables(["a1", "a2", "a3", "a4",
                      "b1", "b2", "b3", "b4",
                      "c1", "c2", "c3", "c4",
                      "d1", "d2", "d3", "d4" ],
                     [1, 2, 3, 4])

distinct_numbers = lambda a1, a2, b1, b2: (
        (a1 != a2) and (a1 != b1) and (a1 != b2) and (a2 != b1) and (a2 != b2) and (b1 != b2));

problem.addConstraint(distinct_numbers, ["a1", "a2", "b1", "b2"])
problem.addConstraint(distinct_numbers, ["a3", "a4", "b3", "b4"])
problem.addConstraint(distinct_numbers, ["c1", "c2", "d1", "d2"])
problem.addConstraint(distinct_numbers, ["c3", "c4", "d3", "d4"])

problem.addConstraint(distinct_numbers, ["a1", "a2", "a3", "a4"])
problem.addConstraint(distinct_numbers, ["b1", "b2", "b3", "b4"])
problem.addConstraint(distinct_numbers, ["c1", "c2", "c3", "c4"])
problem.addConstraint(distinct_numbers, ["d1", "d2", "d3", "d4"])

problem.addConstraint(distinct_numbers, ["a1", "b1", "c1", "d1"])
problem.addConstraint(distinct_numbers, ["a2", "b2", "c2", "d2"])
problem.addConstraint(distinct_numbers, ["a3", "b3", "c3", "d3"])
problem.addConstraint(distinct_numbers, ["a4", "b4", "c4", "d4"])

solution = problem.getSolution()
i = 0
for key in solution:
    if i % 4 == 0:
        print(" ")
    print(key, ":", solution[key], "     ", end="")
    i = i + 1
