import matrix

eq_system = [[5, 2, 3], [4, 5, 6], [7, 8, 9]]
# Right-hand side of the equations
eq_matrix = [-3, 4, 1]
result = matrix.gauss_method(eq_system, eq_matrix)

print (result)
