from math import pow, sqrt  # Actually no need of importing just for power !!   

class Calculator:
    @staticmethod
    def greet():
        print("Hello")

    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"Square of {self.number} is : {pow(self.number, 2)}")

    def sqrt(self):
        print(f"Square root of {self.number} is : {sqrt(self.number)}")     # print(f"Cube of {self.number} is : {self.number ** 0.5}")

    def cube(self):
        print(f"Cube of {self.number} is : {self.number ** 3}")     # Raised to operator in python  

my_calculator = Calculator(9)
my_calculator.square()
my_calculator.cube()
my_calculator.sqrt()
my_calculator.greet()