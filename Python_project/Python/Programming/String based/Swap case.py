# A-Z(65-90)  a-z(97-122)

# Convertingcamel case to snake case
S1 = "Winter Is Coming"
S2 = ""
for i in S1:
    if ord(i) <= 90 and ord(i) >= 65:
        S2 = S2 + chr(ord(i) + 32)
    elif i == " ":
        S2 += "_"
    else:
        S2 += i
print(S2)
