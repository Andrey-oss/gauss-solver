### Gauss Solver ###

This is a **test project** implementing a system of linear equations solver using the Gaussian elimination method. The code includes several helper functions for working with matrices, such as transposition, zero padding, and minor calculations.

⚠️ **Disclaimer:** This project contains a lot of messy and unoptimized code due to my skills and some my algorithms, which I wrote into my notebook :D

🛠 **Note**: This project does not use any third-party libraries—only custom-written algorithms. The idea of my project - write an interesting, useful app with algorithms

⚙️ **Also**: In this project I used some my skills in linear algebra, I didn't see anything in internet or wikipedia. I was solving a lot of problems to do the algorithms in the notebook :D

---

## 📌 Functions Overview

- **`transpose_matrix(matrix)`** – Transposes a matrix (switching rows and columns).
- **`add_zeros(matrix)`** – Adds zeros to the matrix after applying the Gaussian algorithm.
- **`swap(matrix, idx)`** – Swaps matrix rows for correct calculations.
- **`minor(matrix, idx)`** – Computes the minor of a matrix by rearranging rows.
- **`gauss_method_algo(eq_system, eq_matrix, result={})`** – Recursive Gaussian elimination algorithm to reduce the matrix to echelon form and find unknown variables.
- **`gauss_method(eq_system, eq_matrix)`** – Main function to solve a system of linear equations using the Gaussian method.
- **`full_return(matrix)`** – Returns in more legacy solutions.
- **`check_matrix(matrix)`** – Check if matrix is square.

---

## 🚀 How to Use

Example usage:

```python
# Import library
import matrix

# Coefficients of the equation system
eq_system = [[4, -3, 3, -2], [3, 2, 3, 4], [1, 3, -5, 3], [2, -2, 5, -5]]
# Right-hand side of the equations
eq_matrix = [0, 3, 4, 3]

# Run Gaussian method
result = gauss_method(eq_system, eq_matrix)

# Return result
print (result) # [1.0, 2.0, 0.0, -1.0]

# Return in full output
print (matrix.full_return(result)) # {'x1': 1.0, 'x2': 2.0, 'x3': 0.0, 'x4': -1.0}
```

---

## 🎯 Output
The function `gauss_method` solves the system and prints the values of unknown variables.

---

💡 **Found a bug?** Feel free to report it!

## 📜 License
This project is licensed under the **MIT License**.

---