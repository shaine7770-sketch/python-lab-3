# Convert 1/0 input into boolean values.
first = input("Enter the first boolean (1=True, 0=False): ") == "1"
second = input("Enter the second boolean (1=True, 0=False): ") == "1"

print("AND:", first and second)
print("OR:", first or second)
print("NOT first:", not first)

# Show bitwise operations on two integers.
a = 5
b = 3

print("a:", a, bin(a))
print("b:", b, bin(b))
print("AND (&):", bin(a & b))
print("OR (|):", bin(a | b))
print("XOR (^):", bin(a ^ b))
print("NOT (~a):", bin(~a))
print("Left shift (a << 1):", bin(a << 1))
print("Right shift (a >> 1):", bin(a >> 1))