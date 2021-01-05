class Number():
    def __init__(self,n1,n2):
        self.a = n1
        self.b = n2
    def mySum(self):
        sum = self.a + self.b
        return sum

    def inProduct(self):
        p = self.a * self.b
        return p

n = Number(12,15)
print(n.mySum())
print(n.inProduct())