S='A pen, is :Si NeP a'
Result=""

for i in S:
    if ord(i)>=65 and ord(i)<=90:
        Result+=chr(ord(i)+32)
        # print(Result)
    # elif i==" " or i=="," or i==":":
    elif i in " ,:":
        Result+=""
    else:
        Result+=i
print(Result)

# A-Z = 65-90
# a-b = 97-122

