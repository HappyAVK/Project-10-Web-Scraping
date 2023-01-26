import smtplib
import os
from email.message import EmailMessage
import sqlite3



key = os.getenv("PyPass")
sender = "alexlsouthall@yahoo.com"
receiver = "allalexandersouth@gmail.com"

database = sqlite3.connect("data.db")

def read_data(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]

    band, city, date = row

    cursor = database.cursor()
    cursor.execute("SELECT * FROM EVENTS WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows

def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = database.cursor()
    cursor.execute("INSERT INTO EVENTS VALUES(?,?,?)", row)
    database.commit()


def send_mail(tour):

    if tour != "No upcoming tours":
        tour_list = read_data(tour)

        if not tour_list:

            store(tour)

            email_msg = EmailMessage()
            email_msg["Subject"] = "A new tour has arrived!"
            email_msg.set_content(f"{tour} is going to be touring!")

            yahoo = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            yahoo.ehlo()

            yahoo.starttls()

            yahoo.login(sender, key)

            yahoo.sendmail(sender, receiver, email_msg.as_string())

            yahoo.quit()
            print("Sent!")





        else:
            print("Nope")

    return

if __name__ == "__main__":

   # send_mail("blahblahblah")
    print(read_data("On,The,26434"))