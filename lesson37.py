from math import floor


class NumericRangeMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        if key in self.pixel_fields and not (0 <= value <= 255):
            raise ValueError(f"Value of {key} must be in range 0-255")
        else:
            super().__setattr__(key, value)


class Pixel(NumericRangeMixin):
    pixel_fields = ['red', 'green', 'blue']

    def __init__(self, red, green, blue, **kwargs):
        super().__init__(**kwargs)
        self.__red = red
        self.__green = green
        self.__blue = blue

    def __add__(self, other):
        if isinstance(other, Pixel):
            new_red = min(self.__red + other.__red, 255)
            new_green = min(self.__green + other.__green, 255)
            new_blue = min(self.__blue + other.__blue, 255)
            return Pixel(new_red, new_green, new_blue)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Pixel):
            new_red = max(self.__red - other.__red, 0)
            new_green = max(self.__green - other.__green, 0)
            new_blue = max(self.__blue - other.__blue, 0)
            return Pixel(new_red, new_green, new_blue)

    def __rsub__(self, other):
        if isinstance(other, Pixel):
            new_red = max(other.__red - self.__red, 0)
            new_green = max(other.__green - self.__green, 0)
            new_blue = max(other.__blue - self.__blue, 0)
            return Pixel(new_red, new_green, new_blue)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_red = min(floor(self.__red * other), 255)
            new_green = min(floor(self.__green * other), 255)
            new_blue = min(floor(self.__blue * other), 255)
            return Pixel(new_red, new_green, new_blue)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other > 0:
            new_red = floor(self.__red / other)
            new_green = floor(self.__green / other)
            new_blue = floor(self.__blue / other)
            return Pixel(new_red, new_green, new_blue)

    def __eq__(self, other):
        if isinstance(other, Pixel):
            return self.__red == other.__red and self.__green == other.__green and self.__blue == other.__blue
        return False

    def __str__(self):
        return f'Pixel object\n\tRed: {self.__red}\n\tGreen: {self.__green}\n\tBlue: {self.__blue}\n'

    def __repr__(self):
        return f'Pixel({self.__red}, {self.__green}, {self.__blue})'


Pixel1 = Pixel(0, 1, 2)
Pixel2 = Pixel(1, 2, 255)
Pixel3 = Pixel(10, 20, 40)
Pixel4 = Pixel(10, 30, 40)
Pixel5 = Pixel(30, 2, 22)
Pixel6 = Pixel(1, 10, 100)
Pixel7 = Pixel(1, 2, 3)
Pixel8 = Pixel(1, 2, 3)

print(Pixel1 + Pixel2)
print(Pixel3 - Pixel4)
print(Pixel4 - Pixel3)
print(Pixel5 / 3)
print(Pixel6 * 3.5)
print(3.5 * Pixel6)
print(Pixel7 == Pixel8)
