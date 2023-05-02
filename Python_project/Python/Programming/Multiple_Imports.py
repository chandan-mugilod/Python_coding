import sys
import os
import re
import time
print(sys.version)
# print(os.curdir)
# print(os.name)
time.sleep(5)
for x in os.listdir():
    print(x)
pattern="[0-9]?"