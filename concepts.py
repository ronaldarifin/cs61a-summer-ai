class A:
    x, y = 0, 0
    def _init_(self):
        return
class B(A):
    def _init_(self):
        return
class C(A):
    def _init_(self):
        return
    
B.x += 2
A.x += 1

C.x += 5
C.z = 10

ins = C()
print(C.x, C.y, C.z)
ins.x = 2000
ins.y = 3000
ins.z = 4000
print(C.x, C.y, C.z)
print(ins.x,ins.y,ins.z)

insz = C()
print(insz.x,insz.y,insz.z)
print(ins.x)
print(C.x)
print(A.x)