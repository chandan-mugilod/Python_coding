from p1 import one

class two(one):
    b=200
    def __init__(self,x,y):
        super().__init__(x, y)

    def fun2(self):
        print("Function two")

# ob1=two(2,4)
# ob1.func1()
# ob1.fun2()
# print(ob1.a)
# print(ob1.b)
# print(ob1.x)
# print(ob1.y)