# Palendrome (121=121)

N = int(input("Enter a number ->"))
rev = 0
temp=N
while N > 0:
    reminder = N % 10
    rev = reminder + rev * 10
    N = N // 10

if temp == rev:
    print(f"Given number {temp} is Palendrome")
else:
    print(f"Given number {temp} is Not a Palendrome")