grade = float(input("Enter a numeric grade (0-100): "))

# Check the highest cutoff first so each score gets the correct letter.
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your grade is: {letter}")

message = "Great job! You passed." if grade >= 70 else "Keep practicing and try again."
print(message)