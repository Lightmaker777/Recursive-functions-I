# Recursive functions I
# Task 2:
# Recursion with return and instructions after return (non tail-recursive)
# A recursive function named factorial that returns the factorial of a number (the number multiplied by every integer lower than the number and greater than 0).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(0))
print(factorial(1))
print(factorial(10))

