# 1. Класс Figure
class Figure:
    unit = "cm"  # Единица измерения

    def __init__(self):
        pass  # 2. Нет атрибутов уровня объекта

    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area должен быть реализован в подклассе")

    def info(self):
        raise NotImplementedError("Метод info должен быть реализован в подклассе")


# 5. Класс Square
class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # 6. Приватный атрибут

    def calculate_area(self):
        return self.__side_length ** 2  # 7. Площадь квадрата

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}²")


# 9. Класс Rectangle
class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  # 10. Приватные атрибуты
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width  # 11. Площадь прямоугольника

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}²")


# 13. Создание списка из фигур
figures = [
    Square(5),
    Square(10),
    Rectangle(4, 6),
    Rectangle(7, 3),
    Rectangle(9, 2)
]

# 14. Вывод информации по всем фигурам
for figure in figures:
    figure.info()
