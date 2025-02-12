import matrix

def output(result):
    for i in range(len(result)):
        print (f'x{i+1} = {result[i]}')

# Code doesn't solve it, cuz it doesn't have any solutions, so error will be reported
# Uncomment it to test

#system = [[1,2,3], [4,5,6], [7,8,9]]
#solves = [-3, 4, 1]

#matrix.check_matrix(system)
#result = matrix.gauss_method(system, solves)

# Code will solve normally this system of equations 

system = [[11, 2, 3], [3,2,1], [1,2,3]]
solves = [1, 2, 3]

matrix.check_matrix(system)
result = matrix.gauss_method(system, solves)

print (matrix.full_return(result))