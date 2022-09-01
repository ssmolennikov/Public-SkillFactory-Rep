from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print("Площадь прямоугольника 1:", rect_1.get_area())
print("Площадь прямоугольника 2:", rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print("Площадь квадрата:", square_1.get_area_square(), square_2.get_area_square())

circle_1 = Circle(6)

print("Площадь круга:", circle_1.get_area_circle())

figures = [rect_1, rect_2, square_1, square_2, circle_1]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())
