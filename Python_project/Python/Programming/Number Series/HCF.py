N1=int(input("Enter first number"))
N2=int(input("Enter second number"))
HCF=1
min=0
if N1==N2:
    print("Both numbers are equal")
else:
    if N1>N2:
        min=N2
    else:
        min=N1

    for i in range(1,min+1):
        if N1%i==0 and N2%i==0:
            HCF=i

print(f"HCF = {HCF}")

