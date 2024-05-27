import numpy as np

# Define parameters
n = 15
m = 5
k = n - m
g_poly = "10100110111"

# Function to convert polynomial string to list of integers
def poly_to_list(poly):
    return [int(bit) for bit in poly]

# Generating polynomial as list
g = poly_to_list(g_poly)

# Constructing the generating matrix G
G = np.zeros((m, n), dtype=int)
for i in range(m):
    G[i, i:i+len(g)] = g

# Generate all possible information vectors
information_vectors = [np.array(list(np.binary_repr(i, m)), dtype=int) for i in range(2**m)]

# Encode information vectors to form codewords
codewords = [np.dot(info_vector, G) % 2 for info_vector in information_vectors]

# Create a table of codewords
codewords_table = np.array(codewords)

# Output the generating matrix and a fragment of the codewords table
print("Generating Matrix (G):")
print(G)
print("\nFirst 10 Codewords:")
print(codewords_table[:10])

# Calculate t (error correction capability)
d_min = 7
t = (d_min - 1) // 2

# Number of distinct error vectors the code can correct
distinct_error_vectors = sum([np.math.comb(n, i) for i in range(t + 1)])

# Parity-check matrix H (can be derived from G)
# H is (n-k) x n matrix, G is m x n, so H = [I | P^T] where G = [I | P]
H = np.hstack((np.eye(n-m, dtype=int), G[:, m:].T))

# Function to calculate syndrome
def calculate_syndrome(error_vector, H):
    return np.dot(H, error_vector) % 2

# Example error vector
error_vector = np.zeros(n, dtype=int)
error_vector[0] = 1  # Single bit error

syndrome = calculate_syndrome(error_vector, H)

print("\nError Correction Capability (t):", t)
print("Number of Distinct Error Vectors Correctable:", distinct_error_vectors)
print("Syndrome for Error Vector [1,0,...,0]:", syndrome)

# Maximum number of errors guaranteed to be detected
sigma = d_min - 1

# Error vectors that cannot be detected (weight >= d_min)
undetectable_errors = [np.binary_repr(i, n) for i in range(2**n) if bin(i).count('1') >= d_min]

print("\nMaximum Number of Errors Guaranteed to be Detected (σ):", sigma)
print("First 10 Undetectable Errors (weight >= d_min):")
print(undetectable_errors[:10])
