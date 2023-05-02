import re

ip=input("Enter Ip")
# pattern="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
#
# if (re.search(pattern,ip)):
#     print(f"{ip} is valid")
# else:
#     print(f"{ip} is invalid")


Date_validation_pattern= "^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/((19|20)\d\d)$"  #MM/DD/YYYY

if (re.search(Date_validation_pattern,ip)):
    print("yes")
else:
    print("No")








# 255=        25[0-5]
# 200-249=    2[0-4][0-9]
# 100-199=    1[0-9][0-9]
# 0-99=       [1-9]?[0-9]

#1-12=  1[0-2]
#31=    3[0-1]