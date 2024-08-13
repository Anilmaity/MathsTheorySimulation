from pulp import *

#  KNAPSACK PROBLEM


# get max prices with 17 of weight

# data
n  = 8
weights = [4, 2, 8, 3, 7, 5, 9, 6]
prices = [19, 17, 30, 13, 25, 29, 23, 10]
carry_weight = 17

model = LpProblem(sense=LpMaximize)

variables = [LpVariable(name=f"X{i}", cat=LpBinary) for i in range(n)]

model += lpDot(weights, variables) <= carry_weight

model += lpDot(prices, variables)

status = model.solve(PULP_CBC_CMD(msg=False))

print("price", model.objective.value())
print("tasks", *[variables[i].value() for i in range(n)])