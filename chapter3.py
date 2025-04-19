############ Lesson 03: Operators, Keywords & Variables ###########

# 1) **** Arithmetic Operators ****

# Addition (+)
num1 = 10
num2 = 5
result = num1 + num2
print("Addition Result:", result)

# Subtraction (-)
num1 = 10
num2 = 5
result = num1 - num2
print("Subtraction Result:", result)

# Multiplication (*)
num1 = 10
num2 = 5
result = num1 * num2
print("Multiplication Result:", result)

#  Division (/)
num1 = 10
num2 = 5
result = num1 / num2
print("Division Result:", result)

# Modulus (%)
num1 = 10
num2 = 3
result = num1 % num2
print("Modulus Result:", result)

# Floor Division (//)
num1 = 10
num2 = 3
result = num1 // num2
print("Floor Division Result:", result)

#  Exponentiation (**)
num1 = 2
num2 = 3
result = num1 ** num2
print("Exponentiation Result:", result)

# 2) ****   Comparison Operators   ****

# Equal to (==)
num1 = 10
num2 = 10
result = num1 == num2
print("Is num1 equal to num2?", result)

# Not equal to (!=)
num1 = 10
num2 = 5
result = num1 != num2
print("Is num1 not equal to num2?", result)

#  Greater than (>)
num1 = 10
num2 = 5
result = num1 > num2
print("Is num1 greater than num2?", result)

#  Less than (<)
num1 = 5
num2 = 10
result = num1 < num2
print("Is num1 less than num2?", result)

#  Greater than or equal to (>=)
num1 = 10
num2 = 10
result = num1 >= num2
print("Is num1 greater than or equal to num2?", result)

#  Less than or equal to (<=)
num1 = 5
num2 = 10
result = num1 <= num2
print("Is num1 less than or equal to num2?", result)

# 3) ****    Logical Operators     ***

# & Operator
num1 = 10
num2 = 5
num3 = 3

# Check if both conditions are true
result = (num1 > num2) and (num2 > num3)
print("Is num1 > num2 and num2 > num3?", result)

# or Operator
num1 = 10
num2 = 5
num3 = 3

# Check if at least one condition is true
result = (num1 > num2) or (num2 < num3)
print("Is num1 > num2 or num2 < num3?", result)

# not Operator
num1 = 10
num2 = 5

# Check if num1 is not equal to num2
result = not (num1 == num2)
print("Is num1 not equal to num2?", result)

# 4) ****  Assignment Operators  ****

# Basic Assignment (=)
x = 10  # Assigns 10 to variable x
print(x)  # Output: 10

# Addition Assignment (+=)
x = 5
x += 3  # Equivalent to x = x + 3
print(x) # Output: 8

# Subtraction Assignment (-=)
x = 10
x -= 2  # Equivalent to x = x - 2
print(x) # Output: 8

# Multiplication Assignment (*=)
x = 4
x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 8

#  Division Assignment (/=)
x = 20
x /= 4  # Equivalent to x = x / 4
print(x)  # Output: 5.0

# Floor Division Assignment (//=)
x = 20
x //= 3  # Equivalent to x = x // 3
print(x)  # Output: 6

#  Modulus Assignment (%=)
x = 10
x %= 3  # Equivalent to x = x % 3
print(x)  # Output: 1

# Exponentiation Assignment (**=)
x = 2
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 8

# 5) **** Identity Operator ****

# Using is
a = [1, 2, 3]
b = a  # b and a refer to the same object in memory
print(a is b)  # Output: True

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Output: False

# Using is not
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  # Output: True (a and b are different objects in memory)

x = [1, 2, 3]
y = x
print(x is not y)  # Output: False (x and y refer to the same object in memory)

# 6) ****  Membership Operators ****

# Using in
# Example 1: Using `in` with a list
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # Output: True (banana is in the list)
print('grape' in fruits)  # Output: False (grape is not in the list)

# Example 2: Using `in` with a string
text = "Hello, world!"
print('Hello' in text)  # Output: True (Hello is in the string)
print('Python' in text)  # Output: False (Python is not in the string)

# Example 3: Using `in` with a tuple
numbers = (1, 2, 3, 4)
print(3 in numbers)  # Output: True (3 is in the tuple)
print(5 in numbers)  # Output: False (5 is not in the tuple)

#  Using not in
# Example 4: Using `not in` with a list
fruits = ['apple', 'banana', 'cherry']
print('grape' not in fruits)  # Output: True (grape is not in the list)
print('banana' not in fruits)  # Output: False (banana is in the list)

# Example 5: Using `not in` with a string
text = "Hello, world!"
print('Python' not in text)  # Output: True (Python is not in the string)
print('world' not in text)  # Output: False (world is in the string)

# Example 6: Using `not in` with a tuple
numbers = (1, 2, 3, 4)
print(5 not in numbers)  # Output: True (5 is not in the tuple)
print(2 not in numbers)  # Output: False (2 is in the tuple)

# 7) ****  Bitwise operators ****

# Bitwise AND (&)
a = 5   # 0101 in binary
b = 3   # 0011 in binary
result = a & b
print(result)  # Output: 1 (0001 in binary)

#  Bitwise OR (|)
a = 5   # 0101 in binary
b = 3   # 0011 in binary
result = a | b
print(result)  # Output: 7 (0111 in binary)

#  Bitwise XOR (^)
a = 5   # 0101 in binary
b = 3   # 0011 in binary
result = a ^ b
print(result)  # Output: 6 (0110 in binary)

# Bitwise NOT (~)
a = 5   # 0101 in binary
result = ~a
print(result)  # Output: -6 (In two's complement representation)

# Bitwise Left Shift (<<)
a = 5   # 0101 in binary
result = a << 1  # Shifting the bits 1 position to the left
print(result)  # Output: 10 (1010 in binary)

# Bitwise Right Shift (>>)
a = 5   # 0101 in binary
result = a >> 1  # Shifting the bits 1 position to the right
print(result)  # Output: 2 (0010 in binary)

############# *************** #############