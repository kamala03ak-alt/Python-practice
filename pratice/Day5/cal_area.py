class Circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

c1=Circle(int(input("Enter the radius of the circle:")))
print(c1.area())