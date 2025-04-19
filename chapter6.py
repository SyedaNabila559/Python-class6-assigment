#######  Lesson 06: Lists, Tuples & Dictionary ########

### 1.Lists ###

### Creating a List ###

# A list of integers ###
my_list = [1, 2, 3, 4, 5]

# A list with mixed data types ###
mixed_list = [1, "apple", 3.14, True]

### Accessing Elements ###
print(my_list[0])  # Output: 1
print(mixed_list[1])  # Output: "apple"

###  Modifying a List ###
my_list[1] = 10  # Changes the second element to 10
print(my_list)  # Output: [1, 10, 3, 4, 5]

###  Adding Elements ###
my_list.append(6)  # Adds 6 at the end
print(my_list)  # Output: [1, 10, 3, 4, 5, 6]

my_list.insert(2, 7)  # Inserts 7 at index 2
print(my_list)  # Output: [1, 10, 7, 3, 4, 5, 6]

### Removing Elements ###
my_list.remove(7)  # Removes the first occurrence of 7
print(my_list)  # Output: [1, 10, 3, 4, 5, 6]

my_list.pop(2)  # Removes the element at index 2
print(my_list)  # Output: [1, 10, 4, 5, 6]

del my_list[0]  # Deletes the first element
print(my_list)  # Output: [10, 4, 5, 6]

### List Slicing ###
print(my_list[1:3])  # Output: [4, 5]

### Looping through a List ###
for item in my_list:
    print(item)


### 2.Tuples ###

### Creating a Tuple ###
# A tuple of integers
my_tuple = (1, 2, 3, 4, 5)

# A tuple with mixed data types
mixed_tuple = (1, "banana", 3.14, False)

### Accessing Elements ###
print(my_tuple[0])  # Output: 1
print(mixed_tuple[1])  # Output: "banana"

### Tuple Immutability ###
# my_tuple[0] = 10  # This will raise an error because tuples are immutable

### Looping through a Tuple ###
for item in my_tuple:
    print(item)

### Tuple Packing and Unpacking ###
packed_tuple = 1, 2, 3
### Unpacking ###
x, y, z = packed_tuple
print(x, y, z)  # Output: 1 2 3


#### 3.Dictionary ####

### Creating a Dictionary ###
# Creating a dictionary with key-value pairs
student_dict = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student_dict)

### Accessing Dictionary Values ###
# Accessing values by key
print(student_dict["name"])  # Output: Alice
print(student_dict["age"])   # Output: 20

### Adding or Modifying Key-Value Pairs ###
# Adding a new key-value pair
student_dict["major"] = "Computer Science"
print(student_dict)

# Modifying an existing key-value pair
student_dict["age"] = 21
print(student_dict)

###  Removing Key-Value Pairs ###
# Using del to remove a key-value pair
del student_dict["grade"]
print(student_dict)

# Using pop() to remove a key-value pair and get the value
removed_value = student_dict.pop("major")
print(f"Removed value: {removed_value}")
print(student_dict)

### Checking if a Key Exists ###
# Check if a key exists
if "age" in student_dict:
    print("Age exists in the dictionary.")

if "major" not in student_dict:
    print("Major key is not present.")

###  Iterating Over a Dictionary ###
# Looping through keys and values
for key, value in student_dict.items():
    print(f"{key}: {value}")

###### **************** ########