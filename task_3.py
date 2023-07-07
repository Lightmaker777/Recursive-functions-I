# Recursive functions I
# Task 3:
# Recursion with return and instructions after return (non tail-recursive)
# A function called harmonic_sum that requires an integer as an argument.
# The function will return the harmonic sum of the integer.
# The harmonic sum is the sum of reciprocals of the positive integers. 

def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)

print(harmonic_sum(7))
print(harmonic_sum(4))
