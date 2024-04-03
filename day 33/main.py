# # import requests
# #
# # response=requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()
# # data=response.json()["iss_position"]
# # print(data)
import smtplib
import requests
from datetime import datetime
import time

my_email = "malayboy20047@gmail.com"
password = "vkwr ddoj wvru revj"

MY_LAT = 18.5204
MY_LONG = 73.8567


def iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG - 1000 <= iss_longitude <= MY_LONG + 1000 and MY_LAT - 1000 <= iss_latitude <= MY_LAT + 1000:
        return True


def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    print(time_now)
    print(sunrise)

    if time_now >= sunset or time_now <= sunrise:
        return True


# while True:
#     time.sleep(60)
if night() and iss_above():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="malayboy20047@yahoo.com",
                        msg="Subject: LOOK UP \n\n The ISS is above you in the sky ")
    connection.close()

