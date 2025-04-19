############ Lesson 04: Strings & Type Casting ##########

# Strings in Python

#for multi line string use triple quotes '''any string'''
my_string: str = '''Hello,
World!'''
print(my_string)

# Escape Sequence Characters in Python
print("Hello,\b World!") #\b backspace
print("Hello,\tWorld!")  #\t tab
print("Hello, \"World!\"")
print("Hello,\\ World!")


# Performing Differrent Operations on String Object
# 1. Concatenation
my_string = 'Hello, ' + 'World!'
print(my_string)  # Output: Hello, World!

# 2. Indexing
my_string = 'Hello, World!'
print(my_string[0])  # Output: H


# 3. Slicing
my_string = 'Hello, World!'
print(my_string[7:])  # Output: World!


# 4. Length
my_string = 'Hello, World!'
print(len(my_string))  # Output: 13


# 5. Upper Case
my_string = 'Hello, World!'
print(my_string.upper())  # Output: HELLO, WORLD!


# 6. Lower Case
my_string = 'Hello, World!'
print(my_string.lower())  # Output: hello, world!


# Here are some commonly used string methods:
# 1. split()
#  Purpose: Splits a string into a list using a specified delimiter (default is a space).
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 2. join()
#  Purpose: Joins a list of strings into one string using a specified delimiter.
fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)
print(result)  # Output: apple, banana, cherry

# 3. replace()
#  Purpose: Replaces a specified substring with another one.
greeting = "Hello, World!"
new_greeting = greeting.replace("World", "Python")
print(new_greeting)  # Output: Hello, Python!

# 4. find()
# Purpose: Returns the index of the first occurrence of a substring. Returns -1 if not found.
sentence = "Where is the cat?"
index = sentence.find("cat")
print(index)  # Output: 13

# 5. count()
# Purpose: Counts how many times a substring appears.
quote = "You do you, and let them do them."
count = quote.count("do")
print(count)  # Output: 3

# Comparison Operators for Strings in Python
str1 = "apple"
str2 = "banana"
str3 = "Apple"  # Note the capital 'A'

# Equal to
print(f"{str1} == {str2}: {str1 == str2}")     # False

# Not equal to
print(f"{str1} != {str2}: {str1 != str2}")     # True

# Less than
print(f"{str1} < {str2}: {str1 < str2}")       # True (lexicographically)

# Greater than
print(f"{str1} > {str2}: {str1 > str2}")       # False

# Less than or equal to
print(f"{str1} <= {str2}: {str1 <= str2}")     # True

# Greater than or equal to
print(f"{str1} >= {str2}: {str1 >= str2}")     # False

# Compare Two Strings with if-else
str1 = "apple"
str2 = "banana"

if str1 == str2:
    print("Strings are equal.")
elif str1 < str2:
    print(f"{str1} comes before {str2}.")
else:
    print(f"{str1} comes after {str2}.")

####### ********* #######
