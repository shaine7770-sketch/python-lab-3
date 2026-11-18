# Calculate the sum using a for loop.
for_total = 0

for number in range(1, 51):
    if number % 2 == 0:
        for_total += number

print(f"The sum of even numbers from 1 to 50 is {for_total}.")

# Calculate the same sum using a while loop.
while_total = 0
number = 1

while number <= 50:
    if number % 2 == 0:
        while_total += number
    number += 1

print(f"The sum of even numbers from 1 to 50 is {while_total}.")

# Both loops produce 650.
# The for loop is clearer here because the range is known.