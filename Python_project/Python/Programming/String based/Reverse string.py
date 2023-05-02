# S1="kasjh"

# s2=""
# for a in S1:
#     s2=a+s2
#
# print(s2)
s = "abcdklmnoxyz"
S1 = ""
L = []
c = 0
for i in range(1, len(s)):
    if ord(s[i]) - ord(s[i - 1]) == 1:
        S1 += s[i - 1]

    else:
        S1 += s[i - 1]

        L.append(S1)
        S1 = ""
S1 += s[i]
L.append(S1)
print(max(L, key=len))


