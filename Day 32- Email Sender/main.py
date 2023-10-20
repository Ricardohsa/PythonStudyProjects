import datetime as dt
import csv
import random
import smtplib as smtp

current_day = dt.datetime.now()
current_month = current_day.month
current_day = current_day.day
letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

my_email = "python11041982@gmail.com"
password = "hyma kizy koiy pggn"


print(random.choice(letter))

with open("birthdays.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[3] == str(current_month) and row[4] == str(current_day):
            name = row[0]
            email_receiver = row[1]

            with open(f"letter_templates/{random.choice(letter)}") as letter_to_send:
                text = letter_to_send.readlines()
                new_letter = [sub.replace('[NAME]', name) for sub in text]
                new_letter = [sub.replace('\n', '') for sub in new_letter]
                new_letter = [sub.replace('[', '') for sub in new_letter]
                new_letter = [sub.replace(']', '') for sub in new_letter]

                with smtp.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=email_receiver,
                                        msg=f"Subject:Happy Birthday\n\n {new_letter}")

