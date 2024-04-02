##################### Extra Hard Starting Project ######################
import smtplib
import random
import pandas as pd

data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

import datetime as dt

now = dt.datetime.now()
day = now.day
month = now.month
for d in data_dict:
    if month == d['month'] and day == d['day']:
        num = random.randint(1, 3)
        print(num)
        file = open(f"letter_templates/letter_{num}.txt")
        content = file.read()
        old_text = "[NAME],"
        new_text = f"{d['name']},"
        modified_content = content.replace(old_text, new_text)

        with open(f"letter_templates/letter_{num}.txt", 'w') as file:
            file.write(modified_content)
        file = open(f"letter_templates/letter_{num}.txt")
        content = file.read()

        my_email = "malayboy20047@gmail.com"
        password = "vkwr ddoj wvru revj"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="malayboy20047@yahoo.com",
                            msg=f"Subject:Happy Birthday\n\n {content}")
        connection.close()
        file.close()

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
