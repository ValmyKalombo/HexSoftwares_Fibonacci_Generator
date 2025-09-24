# Intermediate Fibonacci Generator
# This program defines a function to return the Fibonacci sequence as a list

def fib(n):
    if n <= 0:
        return "Error: Please enter a positive number."
    
    sequence = [0,1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]  # return only up to n terms

# Example usage
num_terms = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", fib(num_terms))
