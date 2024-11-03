import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(threshold, N_max):
    # Create a grid of complex numbers (x is real part, y is imaginary part)
    x, y = np.mgrid[-2:1:500j, -1.5:1.5:500j]
    c = x + 1j * y

    # Initialize an array (same shape as c) to track the values of z
    z = np.zeros(c.shape, dtype=np.complex128)
    
    # Initialize an array (same shape as c) to track iteration counts for each point
    mask = np.zeros(c.shape, dtype=int)

    # Iterate through each complex number in the grid
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            # Initialize iteration count for this point
            iteration = 0
            
            # Apply the iteration while conditions are satisfied
            while abs(z[i, j]) < threshold and iteration < N_max:
                z[i, j] = z[i, j] ** 2 + c[i, j]  # Update z using the Mandelbrot fractal equation
                iteration += 1
            
            # Update the mask with the number of iterations for this point
            mask[i, j] = iteration

    return mask

def main():
    # Initialize parameters
    threshold = 50  # Set threshold for divergence
    N_max = 100  # Set maximum number of iterations

    # Compute the Mandelbrot set
    mask = mandelbrot(threshold, N_max)

    # Plot the fractal
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5], cmap='gray')
    plt.title("Mandelbrot Set")
    plt.savefig('mandelbrot.png')
    plt.show()

if __name__ == "__main__":
    main()


