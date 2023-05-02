d_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 8}
d_2 = {'c': 4, 'd': 5, 'e': 6}

def merge(d1,d2):
    l=[]
    for x,y in d2.items():
        if x not in d1:
            d1[x]=y
        else:
            l.append(y)
            l.append(d1[x])
            l=list(set(l))
            d1[x]=l
            l=[]
    return d1

a=merge(d_1,d_2)
print(a)

