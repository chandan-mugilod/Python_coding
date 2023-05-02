# To find minimum value in list
L = eval(input("Enter list"))
min = L[0]
for i in range(1, len(L)):
    if min > L[i]:
        min = L[i]
max = L[0]
for i in range(1, len(L)):
    if max < L[i]:
        max = L[i]

print("Maximum value is ->", max)
print("Minimum value is ->", min)
