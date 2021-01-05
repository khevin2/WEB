class Shape():
    def __init__(self,n1,n2):
        self.l = n1
        self.w = n2
class Rectangle(Shape):
    def __init__(self):
        l = int(input("Enter the length"))
        w = int(input("Enter the width"))
        super().__init__(l,w)
    def AreaR(self):
        return self.l * self.w
class Triangle(Shape):
    def __init__(self):
        l = int(input("Enter the length"))
        w = int(input("Enter the width"))
        super().__init__(l,w)
    def AreaT(self):
        return (self.l*self.w)/2

rectangle = Rectangle()
triangle = Triangle()
print(rectangle.AreaR())
print(triangle.areaT())

