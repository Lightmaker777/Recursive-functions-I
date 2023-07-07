# Recursive functions I
# Task 1:
# Recursion with no return (no unwinding).
# A recursive function named countdown with a single integer input argument that prints a countdown starting from the given number.

def countdown(n):
    if n >= 0:
        print(n)
        countdown(n - 1)


countdown(5)
