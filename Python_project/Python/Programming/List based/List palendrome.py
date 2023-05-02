L = eval(input("Enter the list"))
j = len(L) - 1
for i in range(len(L)):
    if L[i] != L[j]:
        print("List is not a palendrome")
        break
    j -= 1
else:
    print("List is palendrome")


