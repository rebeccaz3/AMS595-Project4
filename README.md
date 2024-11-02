# AMS595-Project4
Simulating 3 mathematical phenomenons using Python (Mandelbrot Set, Markov Chain, and Taylor Series Approximation)

**mandelbrot.py**

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
