factorial = (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))

# Example usage:
print(factorial(5))  # Output will be 120
