import smtplib
import random
import datetime as dt
now=dt.datetime.now()
week=now.weekday()
if week==1:
    file = open("quotes.txt", "r")
    content = file.read().splitlines()
    quote=random.choice(content)
    print(quote)



    my_email = "malayboy20047@gmail.com"
    password = "vkwr ddoj wvru revj"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="malayboy20047@yahoo.com",
                        msg=f"Subject:Monday Motivation\n\n{quote}")
    connection.close()
    file.close()


