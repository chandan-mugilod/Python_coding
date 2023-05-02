import re
# l=["jan\n","feb\n"]
# fh=open("/Users/chandanko/PycharmProjects/Python_project/Python/abc.txt","a")
# # b=fh.readline()
# # fh.seek(10)
# # c=fh.readline()
# fh.writelines(l)
# fh.close()
f=open("/Users/chandanko/PycharmProjects/Python_project/Python/abc.txt")
b=f.read()
print(b)
# print(c)

pattern=r"j*n"
res=re.search(pattern,b)
print(res)