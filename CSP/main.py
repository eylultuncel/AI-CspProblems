from constraint import Problem, BacktrackingSolver

print("\n-----------------------------------------\n")
print("PROPOSITIONAL FORMULA 1")
print("\n-----------------------------------------\n")


problem = Problem(BacktrackingSolver())
problem.addVariables(["a", "b", "c", "d"], [True, False])
problem.addConstraint(lambda a, b, c, d: (a | b), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (b | c), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (c | d), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (d | a), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (a | c), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (b | (not c)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (c | (not d)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (d | b), ["a", "b", "c", "d"])
solution = problem.getSolution()
solution = problem.getSolutions()
for i in range(0, len(solution)):
    print(solution[i])


print("\n-----------------------------------------\n")
print("PROPOSITIONAL FORMULA 2")
print("\n-----------------------------------------\n")


problem = Problem(BacktrackingSolver())
problem.addVariables(["a", "b", "c", "d"], [True, False])
problem.addConstraint(lambda a, b, c, d: (a | b | (not c)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (b | c | (not d)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (c | d | (not a)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: ((not a) | (not b) | (not d)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (b | (not c) | (not d)), ["a", "b", "c", "d"])
solution = problem.getSolution()
solution = problem.getSolutions()
for i in range(0, len(solution)):
    print(solution[i])


print("\n-----------------------------------------\n")
print("PROPOSITIONAL FORMULA 3")
print("\n-----------------------------------------\n")


problem = Problem(BacktrackingSolver())
problem.addVariables(["a", "b", "c", "d","e"], [True, False])
problem.addConstraint(lambda a, b, c, d, e: (a | b | (not c)), ["a", "b", "c", "d", "e"])
problem.addConstraint(lambda a, b, c, d, e: ((not b) | d | e), ["a", "b", "c", "d", "e"])
problem.addConstraint(lambda a, b, c, d, e: ((not a) | b | c), ["a", "b", "c", "d", "e"])
problem.addConstraint(lambda a, b, c, d, e: (b | d | (not e)), ["a", "b", "c", "d", "e"])
solution = problem.getSolution()
solution = problem.getSolutions()
for i in range(0, len(solution)):
    print(solution[i])


print("\n-----------------------------------------\n")
print("PROPOSITIONAL FORMULA 4")
print("\n-----------------------------------------\n")


problem = Problem(BacktrackingSolver())
problem.addVariables(["a", "b", "c", "d","e"], [True, False])
problem.addConstraint(lambda a, b, c, d: ((not a) | b), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: ((not b) | c), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: ((not c) | d), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: ((not d) | a), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (a | (not b)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (b | (not c)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d: (c | (not d)), ["a", "b", "c", "d"])
problem.addConstraint(lambda a, b, c, d, e: (d | (not e)), ["a", "b", "c", "d", "e"])
solution = problem.getSolutions()
for i in range(0, len(solution)):
    print(solution[i])

print("\n-----------------------------------------\n")
print("PROPOSITIONAL FORMULA 5")
print("\n-----------------------------------------\n")

problem = Problem(BacktrackingSolver())
problem.addVariables(["e", "y", "l", "u", "t", "n", "c"], [True, False])
problem.addConstraint(lambda e, y, l, u, t, n, c: (e | y | l), ["e", "y", "l", "u", "t", "n", "c"])
problem.addConstraint(lambda e, y, l, u, t, n, c: (l | u | l), ["e", "y", "l", "u", "t", "n", "c"])
problem.addConstraint(lambda e, y, l, u, t, n, c: (t | u | n), ["e", "y", "l", "u", "t", "n", "c"])
problem.addConstraint(lambda e, y, l, u, t, n, c: (c | e | l), ["e", "y", "l", "u", "t", "n", "c"])
problem.addConstraint(lambda e, y, l, u, t, n, c: ((not e) | (not y) | l), ["e", "y", "l", "u", "t", "n", "c"])
problem.addConstraint(lambda e, y, l, u, t, n, c: ((not l) | (not u) | l), ["e", "y", "l", "u", "t", "n", "c"])
problem.addConstraint(lambda e, y, l, u, t, n, c: ((not t) | (not u) | n), ["e", "y", "l", "u", "t", "n", "c"])
problem.addConstraint(lambda e, y, l, u, t, n, c: ((not c) | (not e) | l), ["e", "y", "l", "u", "t", "n", "c"])
solution = problem.getSolutions()
for i in range(0, len(solution)):
    print(solution[i])
print("\n-----------------------------------------\n")

