from pulp import *

# Create the model with maximization objective
model = LpProblem(sense=LpMaximize)

# Define variables
x_p = LpVariable(name="potatoes", lowBound=0)
x_c = LpVariable(name="carrots", lowBound=0)

# Add constraints
model += x_p <= 3000
model += x_c <= 4000

# Define the objective function (linear)
model += 1.2 * x_p + 1.7 * x_c

# Solve the problem
status = model.solve(PULP_CBC_CMD(msg=False))

# Print the results
print("Status:", LpStatus[status])
print("Potatoes:", x_p.value())
print("Carrots:", x_c.value())
print("Objective:", model.objective.value())
