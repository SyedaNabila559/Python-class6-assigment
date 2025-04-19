###### Lesson 07: The Set & Frozenset #######

### 1.Sets ###

# Creating a Set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# You can also create a set from a list or a string
my_set_from_list = set([1, 2, 3, 4, 5, 5])  # Duplicate 5 will be removed
print(my_set_from_list)  # Output: {1, 2, 3, 4, 5}

# Adding Elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing Elements
my_set.remove(4)  # Removes 4 from the set
print(my_set)  # Output: {1, 2, 3, 5, 6}

# Using discard() won't raise an error even if the element doesn't exist
my_set.discard(10)  # No error, even though 10 is not in the set
# using pop
popped_element = my_set.pop()
print(popped_element)  # Output: Some element (sets are unordered)
print(my_set)  # The set with one element removed

# Set Operations
# Union (| or .union()): Combines two sets.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection (& or .intersection()): Returns elements that are common to both sets.
intersection_set = set_a & set_b
print(intersection_set)  # Output: {3}

# Difference (- or .difference()): Returns elements in one set but not in the other.
difference_set = set_a - set_b
print(difference_set)  # Output: {1, 2}

# Symmetric Difference (^ or .symmetric_difference()): Returns elements that are in either set but not both.
symmetric_difference_set = set_a ^ set_b
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


#####  Frozensets ####

# Creating a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})

# Union
frozenset_a = frozenset([1, 2, 3])
frozenset_b = frozenset([3, 4, 5])
union_frozenset = frozenset_a | frozenset_b
print(union_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})

# Intersection
intersection_frozenset = frozenset_a & frozenset_b
print(intersection_frozenset)  # Output: frozenset({3})

# Difference
difference_frozenset = frozenset_a - frozenset_b
print(difference_frozenset)  # Output: frozenset({1, 2})

# Symmetric Difference
symmetric_difference_frozenset = frozenset_a ^ frozenset_b
print(symmetric_difference_frozenset)  # Output: frozenset({1, 2, 4, 5})

######### *************** #############