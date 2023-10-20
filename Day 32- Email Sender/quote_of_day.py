import random as rd
import datetime as dt
import smtplib as smtp

current_day = dt.datetime.now()
my_email = "python11041982@gmail.com"
password = "hyma kizy koiy pggn"
to = "r.humberto.sa@gmail.com"




with open("quotes.txt", "r") as file:
    data = file.read()

    if current_day.weekday() == 0:
        data_into_list = data.replace('"', '').split('\n')

        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to,
                                msg=f"Subject:Moment of Inspiration\n\n {rd.choice(data_into_list)}")