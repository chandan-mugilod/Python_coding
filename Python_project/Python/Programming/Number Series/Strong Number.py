# Strong Number (145 = 1!+4!+5! =145)

N = int(input("Enter the number"))
sum = 0
Temp = N
while N > 0:
    i = 1
    fact = 1
    reminder = N % 10
    while (i <= reminder):
        fact *= i
        i += 1
    sum += fact
    N //= 10
print(sum)
if Temp == sum:
    print("The given number is strong number")
else:
    print("The given number is Not strong number")
