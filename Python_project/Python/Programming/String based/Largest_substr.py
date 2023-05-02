String = "abcdabmnmnqrsabcdefg"
l=[]
s=""
for i in range(1,len(String)):
    if ord(String[i])-ord(String[i-1])==1:
        s+=String[i-1]
    else:
        s+=String[i-1]
        l.append(s)
        s=""
s+=String[i]
l.append(s)
print(s)
print(l)
print(max(l,key=len))
