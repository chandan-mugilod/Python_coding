L = eval(input("Enter the list ->"))
#ascending (>)
#descending (<)
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] < L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
print("The list after sorting - >", L)

# descending=[]
# for a in range(len(L)-1,-1,-1):
#     descending.append(L[a])
# print(descending)
