#Changing the functionality of existinng functioon without changing it's implementation
def smartdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner

@smartdiv
def div(a,b):
    print(a/b)

div(2,4)