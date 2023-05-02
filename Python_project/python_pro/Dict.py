d1 = {"a":1, "b":2, "c":3}
d2 ={"c":5, "d":5, "e":6}

d1.update({"e":17})
print(d1)
"""def dic(d_1,d_2):
    List = []
    for x,y in d_2.items():
        if x not in d_1:
            d_1[x]=y
        else:
            List.append(y)
            List.append(d_1[x])
            List=list(set(List))
            d_1[x]=List
            List=[]
    return d_1
print(dic(d1,d2))"""


"""L = [1, 2, 4, 8, 5]
K = 6
# l=[]
# l1=[]
def add(ls,target):
    l = []
    l1 = []
    for x in range(len(ls)):
        for y in range(len(ls)):
            if x==y:
                continue
            else:
                if ls[x]+ls[y]==target:
                    l.append(ls[x])
                    l.append(ls[y])
                    l1.append(tuple(l))
                    l=[]

    return l1


print(add(L,K))"""