# AMS595-Project4
Simulating 3 mathematical phenomenons using Python 
1. Mandelbrot Set
2. Markov Chain
3. Taylor Series Approximation

## 1. mandelbrot.py

This project explores the Mandelbrot Set, a complex fractal structure, using Python. It employs NumPy for efficient numerical computations and Matplotlib for plotting the resulting fractal. The primary objectives are to generate a grid of complex numbers, test complex number by applying the fractal function until divergence occurs or the maximum number of iterations has been reached, and create a mask that helps plot a visualization to show how quickly complex points diverge. 

**Features**

- Mandelbrot Set Calculation: Computes the Mandelbrot set by iterating complex numbers.

- Visualization: Displays the Mandelbrot set using a grayscale colormap.

**Usage**

- Define Parameters: Adjust the threshold and N_max variables in the main function to control the divergence threshold and the maximum number of iterations, respectively.

- Run the Script: Execute the script directly to generate and display the Mandelbrot set.


**Logic for Conditions of belonging in the Mandelbrot Set**

We cannot test if points diverge after an infinite number of iterations, which is why we must define a large cutoff value, N_max, to simulate the behavior. 

We define the following conditions: 

If |z| < threshold after max # of iterations, the complex point c is considered in the Mandelbrot Set. 

If |z| > threshold before the max # of iterations, the complex point c is considered not in the Mandelbrot Set. 

**Output**

The script will compute the Mandelbrot Set based on the defined parameters.

Then it will plot he results and generate a visualization of the distribution of points (saved as mandelbrot.png).

Points outside the Mandelbrot set, are diverging quickly (black). Points inside the Mandelbrot set are bounded after many iterations (white).

The contrast between these areas highlights the fractal's intricate boundary, where points transition from stability (inside) to rapid divergence (outside).



## 2. markov_chain.py

This project simulates the iterative nature of the Markov chain using a randomly generated transition matrix. It demonstrates how to compute the stationary distribution and assess convergence after multiple iterations.

**Features**

- Random Transition Matrix: Generates a random 5x5 transition matrix where each row sums to 1.

- Probability Distribution: Initializes a random probability distribution vector and normalizes it.

- Iteration: Applies the transition rule iteratively to simulate the Markov process.

- Stationary Distribution: Computes the stationary distribution using eigenvalues and eigenvectors of the transition matrix.

- Convergence Check: Evaluates how closely the final distribution approximates the stationary distribution.


**Usage**

Run the Script: Execute the script to generate the Markov chain simulation. The main function will handle the entire process.

**Output**
The following results are printed in the command window: 

- Transition Matrix P

- Initial Probability Distribution p

- Final Probability Distribution p_50 (applies 50 iterations of transition matrix)

- Stationary Distribution

- Difference between p_50 and Stationary Distribution

- True or False: Do p_50 and the stationary distribution match within 10^(-5)? 


## 3. taylor.py
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

    return x * sp.sin(x)**2 + sp.cos(x)

And the parameters are defined as:

    start = -10
    
    end = 10
    
    degree = 99
    
    fixed_c = 0
