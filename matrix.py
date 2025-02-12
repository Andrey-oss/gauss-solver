def check_matrix(matrix: list): # Check if matrix is square
    # It could be a decorator, but not now :)
    for i in matrix:
        if len(i) != len(matrix):
            raise ValueError("Matrix isn't square")

def transpose_matrix(matrix: list) -> list: # From vertical to horizontal or vica versa
    check_matrix(matrix)
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

def add_zeros(matrix: list) -> list: # Add zeros to matrix after gauss algorithm
    for i in range(len(matrix)):
        for j in range(len(matrix)-len(matrix[i])):
            matrix[i].insert(0, 0)
    return matrix

def swap(matrix: list, idx: int) -> list:
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

def minor(matrix: list, idx: int) -> dict:
    m = {}
    matrix = swap(matrix, idx)
    oc = len(matrix)-1 # Output counter
    m[matrix[0][0]] = [i[-oc:] for i in matrix[-len(matrix)+1:]]
    return m

def full_return(matrix: list, letter='x') -> dict:
    mat = {f'{letter}{i+1}':matrix[i] for i in range(len(matrix))}
    return mat

def gauss_method_algo(eq_system: list, eq_matrix: list, res1=[], res2=[]) -> list:
    check_matrix(eq_system)
    matrix1=[]
    matrix2=[]
    if len(eq_matrix) == 1:
        res1.append(eq_matrix[0])
        res2.append(eq_system[0])
        return res2, res1
    k = 1 # Common divisor to do zeros

    # Firstly we have to do common divisor
    for i in range(len(eq_system)):
        k *= eq_system[i][0]

    # Then we must get multiplication factor
    for i in range(len(eq_system)):
        if eq_system[i][0] == 0:
            raise ValueError("Zero pivot encountered! Try row swapping or check input data. Maybe system doesn't have solutions")
        if type(eq_system[i][0]) != int and type(eq_system[i][0]) != float:
            raise TypeError("Matrix contains non-integer symbols")
        factor = k / eq_system[i][0]

        matrix1.append([eq_system[i][j]*factor for j in range(len(eq_system))])
        matrix2.append(eq_matrix[i]*factor)
    
    # Do some arithmetic operations
    for i in range(len(eq_system)-1):
        matrix1[i+1] = [matrix1[0][j]-matrix1[i+1][j] for j in range(len(eq_system))]
        matrix2[i+1] = matrix2[0]-matrix2[i+1]

    # Write data to result
    #result[matrix2[0]] = matrix1[0] # here is a bug, cuz this are two zeros, only one can be written, and this one is the last. See to hash-table/dict documentation
    res1.append(matrix2[0])
    res2.append(matrix1[0])
    matrix1 = minor(matrix1, 0)[matrix1[0][0]]
    matrix2 = matrix2[1:]
    return gauss_method_algo(eq_system=matrix1, eq_matrix=matrix2, res1=res1, res2=res2)

def gauss_method(eq_system: list, eq_matrix: list) -> list:
    result = gauss_method_algo(eq_system, eq_matrix)
    matrix = transpose_matrix(transpose_matrix(add_zeros([i for i in result[0]]))[::-1]) # What a hell
    solves = [k for k in result[1]][::-1]
    matrix = matrix[::-1]
    result = gauss_method_algo(matrix, solves, res1=[], res2=[])

    '''output = []
    for i in range(len(result[0])):
        output.append(result[1][i]/result[0][i][0])

    output = output[::-1] '''

    output = [result[1][i]/result[0][i][0] for i in range(len(result[0]))][::-1]
    
    return output