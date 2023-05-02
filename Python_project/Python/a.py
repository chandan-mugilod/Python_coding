l=[1,8,6,4]
l1=[4,5,8,5]

l.extend(l1)
print(l)
lis_len=len(l)
x=0
while x < lis_len :
    y=x+1
    while y < lis_len:
        if l[x]>l[y]:
            l[x],l[y]=l[y],l[x]
        y+=1
    x+=1

print(l)