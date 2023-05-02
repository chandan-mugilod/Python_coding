from p2 import two

class three(two):
    c=300
    def __init__(self,x,y,z):
        super().__init__(x, y)
        self.z=z
    def fun3(self):
        print("Function three")

ob2=three(2,4,6)
ob2.func1()
ob2.fun2()
ob2.fun3()
print(ob2.y)
