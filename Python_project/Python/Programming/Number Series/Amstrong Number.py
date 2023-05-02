# Amstrong Number (153 =1^3 + 5^3 + 3^3 =153)

N = int(input("Enter the number->"))
temp = N
sum = 0
power = 0
while N > 0:
    reminder = N % 10
    # print(reminder)
    power += 1
    N //= 10
    # print(N)
N = temp
while N > 0:
    reminder = N % 10
    add = reminder ** power
    sum += add
    N //= 10
if temp == sum:
    print("Number is an Amstrong number")
else:
    print("Number is not an Amstrong number")

