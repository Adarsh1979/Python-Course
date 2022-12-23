# Day9: 3/8 Challenge

# student_scores = {
#     "Harry":81,
#     "Ron":78,
#     "Adarsh":99,
#     "Sahil":74,
#     "Ankit":62
# }

# student_grades = {}

# for student in student_scores :
#     score = student_scores[student]
#     if score>90 and score<=100:
#         student_grades[student] = "Outstanding"
#     elif score>80:
#         student_grades[student] = "Exceeds expectations"
#     elif score>70:
#         student_grades[student] = "Acceptable"
#     else : 
#         student_grades[student] = "Fail"

# for student in student_grades :
#     print(student,end=": ")
#     print(student_grades[student])
#     # or we can also write above two lines as
#     # print(student, ":" ,student_grades[student])






# Nesting dictionary in a dictionary
# travel_log = {
#     "france": {"cities_visited":["Paris","Lille","Dijon"]},
#     "India": {"kharcha": {"Mumbai":"$1000","Delhi":"$500","Manali":"$2000"}},
# }
# print(travel_log["India"]["kharcha"]["Delhi"])






# Day9: 5/8 Challenge

def add_new_country(country_p, visits_p, cities_p):
    new_country = {"country":country_p, "visits":visits_p, "cities":cities_p}
    travel_log.append(new_country)

travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country": "India",
        "visits": 6,
        "cities":["Mumbai","Delhi","Jaipur"]
    },
    {}
]
add_new_country("Pakistan",13,["Lahore","Karachi","Islamabad"])
add_new_country("Sri Lanka",13,["Colambo","Karachi","Islamabad"])
print(travel_log)   