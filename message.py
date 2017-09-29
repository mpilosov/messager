import smtplib
from credentials import *
# CREATE A credentials.py file with string variables gmail_user and gmail_pwd

def send_email(recipient, message):
    TO = recipient if type(recipient) is list else [recipient]
    FROM = 'Anon'
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print '\t Message successfully sent.'
    except:
        print "\t Failed to send message."


