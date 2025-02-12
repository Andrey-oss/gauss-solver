def transpose_matrix(matrix): # From vertical to horizontal or vica versa
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

'''def evaluate_minor(minor_dict, res=0):
    
    !!!IT DOESN'T WORK!!!
    
    key = next(iter(minor_dict))
    print(minor_dict[key])
    if len(minor_dict[key]) == 1:
        print (res)
        return res
    
    evaluate_minor(minor(minor_dict))'''

def add_zeros(matrix): # Add zeros to matrix after gauss algorithm
    for i in range(len(matrix)):
        for j in range(len(matrix)-len(matrix[i])):
            matrix[i].insert(0, 0)
    
    return matrix

def swap(matrix, idx):
    if idx >= len(matrix):
        raise IndexError(f"Index {idx} must be lower than length of matrix {len(matrix)}")
    
    if type(idx) != int:
        raise TypeError("Index must be integer only, not", type(idx))
    
    if idx < 0:
        raise IndexError(f"Index {idx} must be >= 0")

    matrix = transpose_matrix(matrix)

    for i in range(idx+1):
        '''temp_row = matrix[0]
        matrix[0] = matrix[i]
        matrix[i] = temp_row'''
        matrix[0], matrix[i] = matrix[i], matrix[0]
    
    return transpose_matrix(matrix)

def minor(matrix, idx):
    m = {}
    matrix = swap(matrix, idx)
    oc = len(matrix)-1 # Output counter
    m[matrix[0][0]] = [i[-oc:] for i in matrix[-len(matrix)+1:]]
    return m

def gauss_method_algo(eq_system, eq_matrix, result={}):
    matrix1=[]
    matrix2=[]
    if len(eq_matrix) == 1:
        result[eq_matrix[0]] = eq_system[0]
        return result
    k = 1 # Common divisor to do zeros

    # Firstly we have to do common divisor
    for i in range(len(eq_system)):
        k *= eq_system[i][0]

    # Then we must get multiplication factor
    for i in range(len(eq_system)):
        factor = k/eq_system[i][0] # Multiplification factor
        matrix1.append([eq_system[i][j]*factor for j in range(len(eq_system))])
        matrix2.append(eq_matrix[i]*factor)

    for i in range(len(eq_system)-1):
        matrix1[i+1] = [matrix1[0][j]-matrix1[i+1][j] for j in range(len(eq_system))]
        matrix2[i+1] = matrix2[0]-matrix2[i+1]

    result[matrix2[0]] = matrix1[0]
    matrix1 = minor(matrix1, 0)[matrix1[0][0]]
    matrix2 = matrix2[1:]
    return gauss_method_algo(eq_system=matrix1, eq_matrix=matrix2, result=result)

def gauss_method(eq_system, eq_matrix):
    result = gauss_method_algo(eq_system, eq_matrix)
    matrix = transpose_matrix(transpose_matrix(add_zeros([v for v in result.values()]))[::-1])
    solves = [k for k in result.keys()][::-1]
    matrix = matrix[::-1]
    result = gauss_method_algo(matrix, solves, result={})
    return [k/v[0] for k, v in result.items()][::-1]
