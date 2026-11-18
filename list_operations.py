# Create and display the original list.
numbers = [42, 15, 8, 23, 4]
print("Original list:", numbers)

# sorted() creates a sorted copy.
print("Sorted copy:", sorted(numbers))
print("Original list unchanged:", numbers)

# sort() changes the original list.
numbers.sort()
print("Sorted in place:", numbers)

# Add a new integer.
numbers.append(10)
print("After appending 10:", numbers)

# Remove an integer by value.
numbers.remove(23)
print("After removing 23:", numbers)

# Reverse the current order.
numbers.reverse()
print("Reversed list:", numbers)