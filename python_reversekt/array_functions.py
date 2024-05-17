# Creating an array
my_array = [1, 2, 3, 4, 5]

# Accessing elements
print("Accessing elements:")
print("First element:", my_array[0])        # Output: 1
print("Last element:", my_array[-1])         # Output: 5

# Modifying elements
print("Modifying elements:")
my_array[0] = 10
print("Modified array:", my_array)          # Output: [10, 2, 3, 4, 5]

# Array length
print("Array length:")
length = len(my_array)
print("Length of the array:", length)        # Output: 5

# Count occurrences
print("Count occurrences:")
count = my_array.count(2)
print("Occurrences of 2:", count)            # Output: 1

# Append elements
print("Appending elements:")
my_array.append(6)
print("Appended array:", my_array)          # Output: [10, 2, 3, 4, 5, 6]

# Extend with another iterable
print("Extending with another iterable:")
new_elements = [7, 8, 9]
my_array.extend(new_elements)
print("Extended array:", my_array)          # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

# Pop element
print("Popping an element:")
popped_element = my_array.pop(2)
print("Popped element:", popped_element)    # Output: 3
print("Array after pop:", my_array)         # Output: [10, 2, 4, 5, 6, 7, 8, 9]

# Reverse array
print("Reversing array:")
my_array.reverse()
print("Reversed array:", my_array)          # Output: [9, 8, 7, 6, 5, 4, 2, 10]

# Sorting array
print("Sorting array:")
my_array.sort()
print("Sorted array:", my_array)            # Output: [2, 4, 5, 6, 7, 8, 9, 10]

# Finding index of an element
print("\nFinding index of an element:")
index = my_array.index(5)
print("Index of 5:", index)                 # Output: 2

# Removing an element
print("Removing an element:")
my_array.remove(6)
print("Array after removal:", my_array)     # Output: [2, 4, 5, 7, 8, 9, 10]

# Copying array
print("Copying array:")
array_copy = my_array.copy()
print("Copied array:", array_copy)          # Output: [2, 4, 5, 7, 8, 9, 10]

# Clearing array
print("Clearing array:")
my_array.clear()
print("Cleared array:", my_array)           # Output: []
