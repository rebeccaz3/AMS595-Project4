import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
import time


# Part 1: Approximate f using Taylor Series Approximation
def taylor_approximation(func, start, end, degree, fixed_c):
    
    # Parameters: 
    # func: the function to approximate
    # start: the beginning of the interval
    # end: the end of the interval
    # degree: the degree of the Taylor polynomial
    # fixed_c: the point around which to expand

    
    # Use SymPy library to evaluate functions and derivatives
    # Define a symbolic variable
    x = sp.symbols('x')
    
    # Convert the function into a SymPy expression
    sym_func = func(x)

    # Create an array of x values in the specified interval
    x_values = np.linspace(start, end, degree + 1)  # degree = 99, so there are 100 terms 
    
    # Initialize as a NumPy array of zeros to hold the approximated y-values
    approx_values = np.zeros_like(x_values, dtype=float)

    # Calculate the Taylor series approximation
    for n in range(degree + 1):
        # Calculate the n-th derivative at fixed_c using built-in SymPy functions
        derivative_at_c = sym_func.diff(x, n).subs(x, fixed_c)

        # Evaluate the term at each x_value
        term = (derivative_at_c / np.math.factorial(n)) * (x_values - fixed_c) ** n

        # Append each term to the NumPy array
        approx_values += np.array(term, dtype=float) # Convert term to float (to ensure NumPy compatibility)

    # Return the NumPy array of approximated values
    return approx_values


# In[2]:


# Part 2: Test the above taylor_approximation function

# Define the function f(x) = x * sin^2(x) + cos(x)
def f(x):
    return x * sp.sin(x)**2 + sp.cos(x)

# Initialize parameters
start = -10
end = 10
degree = 99
fixed_c = 0

# Obtain the Taylor approximation
approx_values = taylor_approximation(f, start, end, degree, fixed_c)

# Evaluate the actual function on the same x values
x_values = np.linspace(start, end, 100)
actual_values = np.array([f(val) for val in x_values], dtype=float)

# Plot the actual function against the Taylor Approximation
plt.figure(figsize=(10, 6))
plt.plot(x_values, actual_values, label='f(x) = x sin²(x) + cos(x)', color='black')
plt.scatter(x_values, approx_values, color='red', label='Taylor Approximation', s=50)
plt.title('Taylor Series Approximation vs. Actual Function')
plt.xlabel('x')
plt.ylabel('f(x) and approximation')
plt.legend()
plt.grid()
plt.xlim(start, end)
plt.ylim(-9, 8)
plt.savefig('taylor_approx.png')
plt.show()


# In[3]:


# Part 3: Function to run the Taylor approximation for various degrees
def taylor_degrees(func, start, end, initial_degree, final_degree, degree_step, fixed_c):
    # Initialize results matrix
    results = []

    # Iterate over degrees from initial_degree to final_degree
    for degree in range(initial_degree, final_degree + 1, degree_step):
        # Start runtime 
        tic = time.time()

        # Obtain the Taylor approximation
        approx_values = taylor_approximation(func, start, end, degree, fixed_c)
        
        # End runtime
        toc = time.time()
        
        # Calculate elapsed time
        elapsed_time = toc - tic

        # Evaluate the actual function on the same x values
        x_values = np.linspace(start, end, degree + 1)
        actual_values = np.array([func(val) for val in x_values], dtype=float)

        # Calculate the sum of absolute differences
        sum_abs_diff = np.sum(np.abs(actual_values - approx_values))

        # Store results
        results.append({
            'Degree': degree,
            'Sum of Absolute Difference': sum_abs_diff,
            'Computation Time for the Approximation': elapsed_time
        })

    # Create a DataFrame from the results
    df = pd.DataFrame(results)

    # Write the DataFrame to a .csv file
    df.to_csv('taylor_values.csv', index=False)


# Test of taylor_degrees function with specified test parameters
start = -10
end = 10
initial_degree = 50
final_degree = 100
degree_step = 10
fixed_c = 0

# Run the taylor_degrees function (results in taylor_values.csv file)
taylor_degrees(f, start, end, initial_degree, final_degree, degree_step, fixed_c)
