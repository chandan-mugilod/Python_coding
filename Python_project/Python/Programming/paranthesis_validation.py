# s = '({[<>]})'
# l=['()','[]','{}','<>']
# while any(i in s for i in l ):
#     for j in l:
#         s=s.replace(j,'')
#
# if s=='':
#     print("Valid")
# else:
#     print("Not Valid")

s = '({[<>]})'
l=['()','[]','{}','<>']

while any(a in s for a in l):
    for j in l:
         s=s.replace(j,"")

if s=="":
    print("Valid")
else:
    print("Not valid")