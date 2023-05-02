INPUT = [23, 6, 8, 43, 5, 3, 678]
# OUTPUT: [23,43,5,3,6,8,678]

sort_even = []
sort_odd = []

for x in range(len(INPUT)):
    if INPUT[x] % 2 == 0:
        sort_even.append(INPUT[x])
    else:
        sort_odd.append(INPUT[x])
sort_even.sort()
sort_odd.sort(reverse=True)
Final_list = sort_odd + sort_even
print(Final_list)


