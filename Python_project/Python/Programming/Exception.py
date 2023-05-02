Numerator=int(input())
Denominator=int(input())
result=0
try:
    result=Numerator//Denominator
    print(result)
except  ZeroDivisionError as zd:
    print(zd,"Can't divide by Zero")
finally:
    print("code has been executed")