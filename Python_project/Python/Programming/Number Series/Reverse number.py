# Reverse a number

N = int(input("Enter a number ->"))
rev = 0
while N > 0:
    reminder = N % 10
    rev = reminder + rev * 10
    N = N // 10
print(rev)
