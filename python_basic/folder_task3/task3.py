from abc import ABC, abstractmethod
import math

class ShapeValidation:

    @staticmethod
    def validate_positive(value: float, parameter_name: str) -> None:
        if value <= 0:
            raise ValueError(f"{parameter_name} должен быть положительным")

    @staticmethod
    def validate_triangle_sides(a: float, b: float, c: float) -> None:
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны треугольника "
                             "должны быть положительными")
        if max(sides) >= sum(sides) - max(sides):
            raise ValueError("Не выполняется неравенство треугольника")


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def compare_area(self, other: 'Shape') -> str:
        self._validate_comparison(other)
        return self._compare_attributes(other, 'area')

    def compare_perimeter(self, other: 'Shape') -> str:
        self._validate_comparison(other)
        return self._compare_attributes(other, 'perimeter')

    def _validate_comparison(self, other: 'Shape') -> None:
        if not isinstance(other, Shape):
            raise TypeError("Можно сравнивать только с объектами Shape")

    def _compare_attributes(self, other: 'Shape', attribute: str) -> str:
        self_value = getattr(self, attribute)()
        other_value = getattr(other, attribute)()

        if math.isclose(self_value, other_value, rel_tol=1e-9):
            return "равно"
        return "больше" if self_value > other_value else "меньше"


class Square(Shape):

    def __init__(self, side: float) -> None:
        ShapeValidation.validate_positive(side, "Сторона квадрата")
        self._side = side

    def area(self) -> float:
        return self._side ** 2

    def perimeter(self) -> float:
        return 4 * self._side


class Rectangle(Shape):

    def __init__(self, width: float, height: float) -> None:
        ShapeValidation.validate_positive(width, "Ширина прямоугольника")
        ShapeValidation.validate_positive(height, "Высота прямоугольника")
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)


class Triangle(Shape):

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        ShapeValidation.validate_triangle_sides(side_a, side_b, side_c)
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def area(self) -> float:
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(
            semi_perimeter *
            (semi_perimeter - self._side_a) *
            (semi_perimeter - self._side_b) *
            (semi_perimeter - self._side_c)
        )

    def perimeter(self) -> float:
        return self._side_a + self._side_b + self._side_c


class Circle(Shape):

    def __init__(self, radius: float) -> None:
        ShapeValidation.validate_positive(radius, "Радиус окружности")
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius


def demonstrate_shapes() -> None:
    try:
        square = Square(5)
        rectangle = Rectangle(4, 6)
        triangle = Triangle(3, 4, 5)
        circle = Circle(3)

        print(f"Квадрат: S = {square.area()}, P = {square.perimeter()}")
        print(f"Прямоугольник: S = {rectangle.area()}, "
              f"P = {rectangle.perimeter()}")
        print(f"Треугольник: S = {triangle.area():.2f}, "
              f"P = {triangle.perimeter()}")
        print(f"Круг: S = {circle.area():.2f}, P = {circle.perimeter():.2f}")
        print(f"\nСравнения:")
        print(f"S квадрата vs прямоугольника: "
              F"{square.compare_area(rectangle)}")
        print(f"S квадрата vs круга: {square.compare_area(circle)}")
        print(f"P квадрата vs круга: {square.compare_perimeter(circle)}")
        print(f"P прямоугольника vs круга: "
              f"{rectangle.compare_perimeter(circle)}")
        print(f"S треугольника vs круга: {triangle.compare_area(circle)}")

    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    demonstrate_shapes()
