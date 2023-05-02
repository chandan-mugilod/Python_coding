from p4 import one


class two(one):
    def fun(self):
        print("Class two")
        super().fun()


ob1 = two()
ob1.fun()
