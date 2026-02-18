# Taking four inputs
a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))
c = int(input("Enter value for C: "))
d = int(input("Enter value for D: "))

if c > d:
    # Find first digit of A
    first_digit = int(str(a)[0])
    
    # Compute A - (first_digit - 1)
    result = a - (first_digit - 1)
    
    print(result)
else:
    print(b)
