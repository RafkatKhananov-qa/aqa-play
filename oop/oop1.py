class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        return f"Brand: {self.brand}, speed: {self.speed}"
