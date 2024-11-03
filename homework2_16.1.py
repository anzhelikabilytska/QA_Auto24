from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

def display_figure_info(figures):
    for figure in figures:
        print(f"Area: {figure.get_area():.2f}, Perimeter: {figure.get_perimeter():.2f}")

rect = Rectangle(15, 30)
circle = Circle(10)

display_figure_info([rect, circle])