# -*- coding: utf-8 -*-
"""OTP_verification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1thXelIExvQfb6BKXeHeozZkGW_CMbynB

**OTP Verification Using Python**
"""

# code by Ireddi Rakshitha
import random
import smtplib
sender_mail = "ireddirakshitha@gmail.com"
password = "yswmpfekmatgauan"
print("=============OTP Verification===============")
receiver_mail = input("Enter your mail:- ")
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_mail,password)
otp = "".join([str(random.randint(0,9)) for i in range(6)])
msg = "Hello, your otp is " + str(otp)
server.sendmail(sender_mail,receiver_mail,msg)
server.quit()
print("OTP sent successfully")
user_otp = input("Enter the OTP sent to your email: ")
if user_otp == otp:
    print("OTP is verified successfully!")
else:
    print("Wrong OTP, enter correct OTP")
    print("Your OTP was:- " + str(otp))