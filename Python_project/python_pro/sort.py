l = [1, 2, 432, 5, 3, 5, 6, 3, 4]

# selection sort

"""for x in range(len(l)):
    for y in range(x+1,len(l)):
        if l[x]>l[y]:
            l[x],l[y]=l[y],l[x]

print(l)"""

# Bubble sort

for x in range(len(l)):
    for y in range(len(l) - x - 1):
        if l[y] > l[y + 1]:
            l[y], l[y + 1] = l[y + 1], l[y]

print(l)
