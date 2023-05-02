dec=int(input())

bi=0
temp=1

while dec>0:
    rem=dec%2
    bi=bi+rem*temp
    temp*=10
    dec//=2
print(bi)