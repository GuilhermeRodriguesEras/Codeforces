from pulp import *

prob = LpProblem("Simple_Problem", LpMinimize)
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

prob += x1 + 3*x2
prob += x1 + 2*x2 >= 6
prob += x1 - x2 <= 3

prob.solve()

print ('x1={} , x2 ={}'.format(value(x1), value(x2)))
