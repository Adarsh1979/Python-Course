# Demo of unlimited positional arguments (positional becoz the type of arguments is Tuple i.e. can be accessed by index)

# def add(*args):     # This * is used to tell that this function can have unlimited arguments (in the form of a tuple)
#     print(type(args))
#     total = 0
#     for i in args:
#         total += i
#     return total
#
#
# print(add(3, 4, 7, 8))      # here the tuple of arguments would be (3,4,7,8)
# ---------------------------------------------------------------------------------------------------------------------#


# ---------------------------------------------------------------------------------------------------------------------#
# Demo of unlimited keyword arguments (keyword becoz here the type of arguments is dictionary)
# example1:

# def calculate(n, **kwargs):
#     n += kwargs["add"]      # if we will provide key by this method to get value of dictionary, then it will throw an
#     #                           error if this argument is not given in the function call.
#     n *= kwargs.get("mul")  # while if we use .get() to access value, then even if we do not give this argument, it
#     #                            won't throw an error, and it will consider its value to be "none".
#     #                            Can be optional (but here due to integer value calculation, it is required)
#     return n


# print(calculate(3))       # won't work
# print(calculate(3, add=5, mul=6))       # works perfectly & dict of args would be {add:5, mul:6}


# example2:
class Car:
    def __init__(self, **kw):
        self.company = kw["company"]        # Necessary argument
        self.model = kw.get("model")        # Optional argument (default value of model argument will be none)
        self.colour = kw.get("colour")      # Optional argument (default value none)


# my_car1 = Car(company="Suzuki")       # allowed
# print(my_car1.company, my_car1.model, my_car1.colour)

# my_car2 = Car(model="Ertiga", colour="white")     # NOT allowed
# print(my_car2.company, my_car2.model, my_car2.colour)

# my_car3 = Car(company="Nissan", model="GT-R", colour="Black")     # Allowed
# print(my_car3.company, my_car3.model, my_car3.colour)

