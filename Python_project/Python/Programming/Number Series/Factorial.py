# Factorial (3!=3*2*1)

N=int(input("Enter a value ->"))
fact=1
for i in range(1,N+1):
    fact*=i

print(fact)