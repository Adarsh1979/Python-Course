import requests
from datetime import datetime
import smtplib


MY_EMAIL = "adarsh@gmail.com"
MY_PASSWORD = "helloworld"
MY_LAT = 51.507351      # 40
MY_LONG = -0.127758     # 15


def is_iss_overhead():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")      # API endpoint
    response1.raise_for_status()
    data1 = response1.json()      # this returns json data (dictionary)

    iss_latitude = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])

    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True
    else:
        return False


def is_dark():
    current_time_hour = datetime.now().hour
    parameters = {
        "lat": MY_LAT,     # this fetches the wrong data from API ( DOUBT )
        "lng": MY_LONG,
        "formatted": 0
    }

    response2 = requests.get(url="https://api.sunrise-sunset.org/json?formatted=0", params=parameters)
    data2 = response2.json()
    sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])

    if current_time_hour >= sunset or current_time_hour <= sunrise:
        return True
    else:
        return False


if is_iss_overhead() and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Look Up👆🏻 \n\n The ISS is above you in the sky."
                            )


