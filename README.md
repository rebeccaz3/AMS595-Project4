# AMS595-Project4
Simulating 3 mathematical phenomenons using Python (Mandelbrot Set, Markov Chain, and Taylor Series Approximation)

## mandelbrot.py

This project explores the Mandelbrot Set, a complex fractal structure, using Python. The primary objectives are to generate a grid of complex numbers, test complex number by applying the fractal function until divergence occurs or the maximum number of iterations has been reached, and create a mask that helps plot a visualization to show how quickly complex points diverge. 

**mandelbrot(threshold, N_max)**

Parameters: 
- threshold : the threshold for divergence
- N_max : the maximum number of iterations

**Logic for Conditions of belonging in the Mandelbrot Set**

We cannot test if points diverge after an infinite number of iterations, which is why we must define a large cutoff value, N_max, to simulate the behavior. 
We define the following conditions: 
If |z| < threshold after max # of iterations, the complex point c is considered in the Mandelbrot Set. 
If |z| > threshold before the max # of iterations, the complex point c is considered not in the Mandelbrot Set. 

**Output**

The script will generate a visualization of the Mandelbrot Set, showcasing the distribution of points.
Points outside the Mandelbrot set, are diverging quickly (black). Points inside the Mandelbrot set are bounded after many iterations (white).
The contrast between these areas highlights the fractal's intricate boundary, where points transition from stability (inside) to rapid divergence (outside).



## markov_chain.py

This project simulates the iterative nature of the Markov Chain using Python. The primary objectives are to generate a random transition matrix & initial probability vector, and normalize them to make them valid distributions. Then apply the transition matrix to the probability vector 50 times (like a Markov Chain), and compare the final probability vector to the stationary distribution to determine if the 2 distirbutions are sufficiently close. 

**Output**
The following results are printed in the command window: 
- Transition Matrix P
- Initial Probability Distribution p
- Final Probability Distribution p_50 (applies 50 iterations of transition matrix)
- Stationary Distribution
- Difference between p_50 and Stationary Distribution
- True or False: Do p_50 and the stationary distribution match within 10^(-5)? 


## taylor.py
This project implements a Taylor Series approximation for a given function and evaluates the accuracy of the approximation over a specified interval. It also visualizes the results and logs the computation details for various degrees of approximation.

**Features**

- Taylor Series Approximation: Approximate a function using its Taylor series around a specified point.
- Visualization: Compare the actual function with its Taylor approximation using Matplotlib.
- Performance Analysis: Measure and log the accuracy and computation time for different degrees of Taylor series.


**Usage**
- Function Definition: You may define the function you wish to approximate.
- Set Parameters: You may define the parameters for the Taylor approximation, including the interval, degree, and point of expansion.


**Outputs**
- A plot comparing the original function and its Taylor approximation.
- A CSV file (taylor_values.csv) containing the sum of absolute differences and computation times for each degree tested.

**Example Plot**
In the provided example, the function is defined as:
def f(x):
    return x * sp.sin(x)**2 + sp.cos(x)

And the parameters are defined as:
start = -10
end = 10
degree = 99
fixed_c = 0
