########### Lesson 02: Data Types ###########

# 1. Numeric Types

# Python has three main numeric types:

# a. Integer (int)
# Whole numbers, positive or negative, without decimals.
num_int: int = 42

print(type(num_int)," num_int = ",num_int,)  # <class 'int'>

# b. Floating-Point (float)
# Numbers with decimal points.
num_float: float = 3.14
#num_float: float = .14

print(type(num_float), " num_float = ", num_float)  # <class 'float'>

# c. Complex (complex)
# Numbers with a real and imaginary part.
num_complex: complex = 2 + 3j

print(type(num_complex), " num_complex = ", num_complex)  # <class 'complex'>

# 2. Boolean (bool)
# Represents True or False.
is_python_fun: bool = True #False

print(type(is_python_fun), " is_python_fun = ", is_python_fun)  # <class 'bool'>

# 3. Sequence Types
# These store multiple items in an ordered way.

# a. String (str)
# A sequence of characters enclosed in quotes.

text_double: str  = "Hello, Python!" # Strings with Double Quotes (")
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, Python!''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    # <class 'str'>
print(type(text_single), " text_single   = ", text_single)    # <class 'str'>
print(type(text_multi), " text_multi    = ", text_multi)      # <class 'str'>
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)  # <class 'str'>

# b. List (list)
# An ordered, mutable collection.
my_list_1: int = [1, 2, 3, "Java", 3.14, True] #Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'
my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]

print(type(my_list_1), " my_list_1 = ", my_list_1)  # <class 'list'>
print(type(my_list), " my_list   =  " + str(my_list)) # we will look into type casting in classes ahead

# c. Tuple (tuple)
# An ordered, immutable collection.
my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3 , 3+2j )
print(type(my_tuple), " my_tuple = ", my_tuple )  # <class 'tuple'>

# d. Range (range)
# Represents a sequence of numbers.
num_range: range = range(1, 10, 2) # range(start, stop, step)
print(type(num_range), " num_range = ", num_range.step)  # <class 'range'>

# 4. Set Types
# (We will cover this indepth in classes ahead)

# Unordered collections with unique elements.

# a. Set (set)
# Mutable, unordered, and contains unique values.
my_set: set = {1, 2, 33, 4, 4, 5}
print(type(my_set), "my_set = ", my_set)  # <class 'set'>

# b. Frozen Set (frozenset)
# Immutable version of a set.
frozen_set = frozenset([11, 2, 3, 4, 4, 5])
#frozen_set = frozenset(my_set)
print(type(frozen_set), " frozen_set = ", frozen_set)  # <class 'frozenset'>

# 5. Mapping Type
# Dictionary (dict) Stores key-value pairs
my_dict: dict = {"name": "Alice", "age": 25, "language": "Python"}
print(type(my_dict)," my_dict = ", my_dict )  # <class 'dict'>

# 6. Binary Types
# a.Bytes (immutable)
b = b"hello"            # Binary literal
print(b[0])             # Output: 104 (ASCII for 'h')

# b.Bytearray (mutable)
ba = bytearray(b)
ba[0] = 72              # Change 'h' to 'H'
print(ba)  

########### **************** #############