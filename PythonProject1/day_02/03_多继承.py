class A:
    def a(self):
        print("a")

class B():
    def b(self):
        print("b")

class C(A,B):
    pass

c = C()
c.a()
c.b()