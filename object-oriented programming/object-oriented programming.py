class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result_area = None
        self.result_perimeter = None

    def solve_perimeter(self):
        return "text"

    def solve_area(self):
        self.result_area = self.a * self.b

    def display_perimeter(self):
        print(self.result_perimeter)


class Rectangles:
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def all_rectangles(self):
        for recatngle in self.rectangles:
            print(recatngle.a, recatngle.b)


recatngle1 = Rectangle(5, 6)
recatngle2 = Rectangle(2, 4)
rectangles = Rectangles([recatngle1, recatngle2])
rectangles.all_rectangles()

