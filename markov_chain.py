import numpy as np

def main():
    # Construct a random 5x5 matrix P
    P = np.random.rand(5, 5)  
    
    # Normalize each row of the matrix
    for i in range(P.shape[0]):
        P[i] /= np.sum(P[i])

    # Construct a random size-5 vector p
    p = np.random.rand(5)
    
    # Normalize the vector
    p /= np.sum(p)
    
    # Create a copy of vector p to manipulate with the transition rule
    p_new = p.copy()
    
    # Apply the transition rule 50 times
    for _ in range(50):
        p_new = np.dot(P.T, p_new)

    # Compute the eigenvalues & eigenvector of P^T
    eigenvalues, eigenvectors = np.linalg.eig(P.T)
    
    # Find the index of the eigenvalue 1
    index1 = np.argmin(np.abs(eigenvalues - 1))

    # Extract eigenvector corresponding to the eigenvalue 1 (only real component)
    v = eigenvectors[:, index1].real
    
    # Normalize v to obtain stationary distribution
    stationary_distribution = v / np.sum(v)

    # Compute the component-wise difference between p50 and the stationary distribution
    difference = np.abs(p_new - stationary_distribution)

    # Check if each element matches within 10^(-5)
    matches = np.all(difference < 1e-5)

    # Print results
    print("Transition Matrix P:\n", P)
    print()
    print("Initial Probability Distribution p:\n", p)
    print()
    print("Final Probability Distribution p_50 (applies 50 iterations of transition matrix):\n", p_new)
    print()
    print("Stationary Distribution:\n", stationary_distribution)
    print()
    print("Difference between p_50 and Stationary Distribution:\n", difference)
    print()
    print("Do p_50 and the stationary distribution match within 10^(-5)?", matches)

if __name__ == "__main__":
    main()