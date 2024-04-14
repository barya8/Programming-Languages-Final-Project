"""
An example program in our language that showcases its capabilities.
The program calculates the factorial of a number using a while loop,
checks if the result is even or odd using conditional logic,
and performs some additional arithmetic operations.
"""

# Factorial of a number
n = 5
factorial = 1
counter = n

print("factorial:", factorial, ",counter:", counter)

while counter > 1:
    factorial = factorial * counter
    counter = counter - 1
    print("factorial:", factorial, ",counter:", counter)

# Check if factorial is even or odd
if factorial % 2 == 0:
    result = "even"
    
else:
    result = "odd"

print ("factorial", factorial, "is:", result)

# Additional calculations
a = 10
b = 20
sum = a + b
difference = b - a
product = a * b
quotient = b // a

# Nested conditionals
if sum > 15:
    if difference < 10:
        nested_result = "nested 1"
    else:
        nested_result = "nested 2"
else:
    if product > 100:
        nested_result = "nested 3"
    else:
        nested_result = "nested 4"

print(nested_result)

# Another loop for countdown
countdown = 5
while countdown > 0:
    countdown = countdown - 1
    if countdown == 2:
        break

print("countdown stoped at:", countdown)

# Final results
final_result = factorial + sum + product
print("factorial:", factorial, ",sum:", sum, ",product:", product)
print ("final result is:", final_result)