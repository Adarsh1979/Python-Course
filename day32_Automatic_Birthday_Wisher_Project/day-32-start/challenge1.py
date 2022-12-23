import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt", encoding="utf8") as file:
        list_of_quotes = file.readlines()
        quote = random.choice(list_of_quotes)

        print(quote)

        # my_email = "helloworld41234@gmail.com"
        # my_password = "hellopython@123"

        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=my_password)
        #     connection.sendmail(from_addr=my_email,
        #                         to_addrs=my_email,
        #                         msg=f"Subject: Monday motivation\n\n{quote}"
        #                         )
