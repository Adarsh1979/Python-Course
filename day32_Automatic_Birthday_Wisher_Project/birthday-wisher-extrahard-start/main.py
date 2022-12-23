# #################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


# Automatic Birthday Wisher Project

import smtplib
import pandas
import datetime
from random import randint

now = datetime.datetime.now()
day = now.day
month = now.month
my_email = "adarsh@gmail.com"
my_password = "helloworld"

data = pandas.read_csv("birthdays.csv")
print(data)
data_list = data.to_dict(orient="records")
print(data_list)

for item in data_list:
    if item["day"] == day and item["month"] == month:
        birthday_email = item["email"]

        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as file:
            file_data = file.read()
            new_letter = file_data.replace("[NAME]", item["name"])

            print(new_letter)
            # with smtplib.SMTP("smtp.gmail.com") as connection:
            #     connection.starttls()
            #     connection.login(user=my_email, password=my_password)
            #     connection.sendmail(from_addr=my_email,
            #                         to_addrs=birthday_email,
            #                         msg=f"Happy Birthday !!\n\n{new_letter}"
            #                         )
