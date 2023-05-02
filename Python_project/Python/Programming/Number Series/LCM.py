N1 = int(input("Enter first number"))
N2 = int(input("Enter second number"))
LCM = 0
max = 0
if N1 > N2:
    max = N1
else:
    max = N2

while True:
    if max % N1 == 0 and max % N2 == 0:
        LCM = max
        break
    max += 1
print(f"LCM = {LCM}")

