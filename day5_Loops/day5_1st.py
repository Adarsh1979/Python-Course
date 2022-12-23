# Day5: 3/9 Challenge
# student_heights = input("Input a list of student's heights \n").split()
# for n in range(0, len(student_heights)) :
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# no_of_students = 0
# for student in student_heights :
#     no_of_students += 1
# # print(no_of_students)

# total_height = 0
# for height in student_heights :
#     total_height += height
# # print(total_height)

# avg_height = round(total_height/no_of_students)
# print(f"Average height of students is {avg_height}")





# Day5: 4/9 Challenge
# student_scores = input("Input a list of student scores : ").split()
# for n in range (0, len(student_scores)) :
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# max = student_scores[0]
# for score in student_scores :
#     if score > max :
#         max = score
# print(f"Highest score is {max}")





# Day5: 6/9 Challenge 
# sum = 0
# for num in range(2,101,2) :
#     sum += num
# print(sum)




# Day5 : 7/9 Challenge
for number in range (1,101) :
    if (number % 3 == 0) and (number % 5 == 0) :
        print("FizzBuzz")
    elif number % 3 == 0 :   
        print("Fizz")
    elif number % 5 == 0 :
        print("Buzz")
    else :
        print(number)