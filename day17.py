
# question 1
class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        return 30

    def m2(self):
        return 40

class C(B):
  
    def m2(self):
        return 20
obj1=A()
obj2=B()
obj3=C()
print(obj1.m1() + obj3.m1()+ obj3.m2())

# question 2
class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        val=super().m1()+30
        return val

class C(B):
    # Method overiding aafnai method lai call gareko garei garxa
    def m1(self):
        val=self.m1()+20
        return val
obj=C()
print(obj.m1())