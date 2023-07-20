class C:
    x = 'e'
    def f(self, y):
        self.x = self.x + y
        return self
    def __str__(self):
        return 'go'
class Big(C):
    x = 'u'
    def f(self, y):
        C.x = C.x + y
        return C.f(self, 'm')
    def __repr__(self):
        return '<bears>'
m = C().f('i')
n = Big().f('o')