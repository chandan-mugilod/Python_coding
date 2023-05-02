# Fibonacci series ( 0, 1, 1, 2, 3, 5, 8.......)

N = int(input("Enter a number ->"))

a, b=0, 1

for i in range(1,N+1):
    print(a, end=" ")
    c=a+b
    a = b
    b = c