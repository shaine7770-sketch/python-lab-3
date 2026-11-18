numbers = [64, 25, 12, 22, 11]
print("Original list:", numbers)

# Each pass moves the largest remaining number to the right.
for i in range(len(numbers) - 1):

    # Compare adjacent numbers, skipping the already sorted end.
    for j in range(len(numbers) - 1 - i):

        # Swap the pair if the left number is larger.
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f"Pass {i + 1}:", numbers)

print("Sorted list:", numbers)