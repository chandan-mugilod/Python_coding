# Disaurium Number (175 = 1^1 + 7^2 + 5^3 = 175)
N = int(input("Enter a number->"))
temp = N
sum = 0
count = len(str(N))
while N > 0:
    reminder = N % 10
    add = reminder ** count
    sum += add
    count -= 1
    N //= 10
if temp == sum:
    print("Number is Disaurium Number")
else:
    print("Number is not a Disaurium Number")
