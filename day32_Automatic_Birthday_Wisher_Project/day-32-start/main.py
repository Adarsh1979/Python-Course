# demo of Sending an Email using smtplib module

# below code is not working because of security reasons of google
# import smtplib
#
# my_email = "helloworld41234@gmail.com"
# my_password = "hellopython@123"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs="knowledgegrowth20@gmail.com", msg="Hello")
# connection.close()


# demo of datetime module

import datetime as dt

current_time = dt.datetime.now()        # calling now() method of datetime class to get the current timestamp
print(type(current_time))
print(current_time)

year = current_time.year        # we can tap into year, month and day from current_time
month = current_time.month
day = current_time.day

print(day)
print(month)
print(year)


day_of_week = current_time.weekday()
print(day_of_week)

# we can also create our datetime object like DOB
date_of_birth = dt.datetime(day=1, month=1, year=2022, hour=18, minute=57, second=12)
print(date_of_birth)
