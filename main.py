import random
import smtplib
import ssl
otp = random.randint(100000, 999999)
otp_str = str(otp)
def send_email(receiver_email, otp):
    sender_email = ""
    sender_password = ""
    message = "Subject: OTP Verification\n\nYour OTP is " + otp
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        print("OTP sent successfully!")
        server.quit()
    except Exception as e:
        print("Error occurred: ", e)
user_email = input("Enter your email address: ")
send_email(user_email, otp_str)
while True:
    user_otp = input("Enter the OTP you received: ")
    if user_otp == otp_str:
        print("Verification successful!")
        break
    else:
        print("Verification failed. Please try again.")
