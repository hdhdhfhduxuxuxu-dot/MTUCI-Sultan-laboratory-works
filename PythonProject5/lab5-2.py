class circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return f"Радиус - {self.radius}"

    def set_radius(self, new_radius):
        self.radius = new_radius


circle1 = circle(20)
print(circle1.get_radius())

try:
    n = int(input("Задайте радиус: "))
except ValueError:
    print("Недопустимое значение")

circle1.set_radius(n)
print(circle1.get_radius())