# Challenge 8.1 4/10 --> Paint calc

# def paint_calc(height, width, cover) :
#     no_of_cans = round((height * width)/cover)
#     print(f"You will need {no_of_cans } cans of paint")

# test_h = int(input("Height of wall : "))
# test_w = int(input("Height of wall : "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)





# Challenge 8.2 5/10 --> Prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2,number-1) :
        if number % i == 0 :
            is_prime = False
    
    if is_prime :
        print("It's a prime")
    else :
        print("It's not a prime number")
prime_checker(number=int(input("Enter number to be checked : ")))
