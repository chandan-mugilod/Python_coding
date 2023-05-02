s="abdba"
y=len(s)-1
for x in range(len(s)-1):
    if s[x] != s[y]:
        print("Not a palendrome")
        break
    # x +=1
    y-=1
else:
    print("Palendrome")
