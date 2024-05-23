class Garage:

    def __init__(self, model: str, engine: int, mileage: int, color: str, year: int):

        self.model = model
        self.engine = engine
        self.mileage = mileage
        self.color = color
        self.year = year


    def car_info(self):
        """
        method returns car info
        :return: string of car info
        """

        return (f'{self.model} {self.year}:'
                f'\nEngine - {self.engine}'
                f'\nMileage - {self.mileage} км'
                f'\nColor - {self.color}')

    def compare_mileages(self, other_car):
        """
        The method compares mileage of the specified cars
        :param other_car:
        :return:
        """
        if self.mileage > other_car.mileage:
            return f'Mileage {self.model} greater than {other_car.model}'
        else:
            return f'Mileage {self.model} less than {other_car.model}'

    @classmethod
    def add_car(cls, model: str, engine: int, mileage: int, color: str, year: int):
        """
        method creates a new instance of the class
        :param model: model of new car
        :param engine: engine of new car
        :param mileage: mileage of new car
        :param color: color of new car
        :param year: manufactured of new car
        :return: new instance of the class
        """
        return cls(model, engine, mileage, color, year)



bmw = Garage('BMW X6', 3.5, 80000, 'Black', 2020)
print(bmw.car_info())
mercedes = Garage('Mercedes GLE 350', 4, 100000, 'Gray', 2019)
print(mercedes.car_info())

print(bmw.compare_mileages(mercedes))

mazda = Garage.add_car('Mazda CX-5', 3.5, 60000, 'White', 2021)
print(mazda.car_info())

