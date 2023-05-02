L=eval(input("Enter list->"))
L1=[]
for i in range(len(L)-1,-1,-1):
    L1.append(L[i])
print(L1)