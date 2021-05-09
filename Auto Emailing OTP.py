import smtplib
import random

otp = ""
for i in range(4):
    otp += str(random.randint(1, 9))  # += is adding the value to the OTP variable


mail = smtplib.SMTP('smtp.gmail.com', 587)
type(mail)
mail.ehlo()
mail.starttls()

def Password():  # Creating Function for Reading Password file. 
    a = open('Password.txt', 'r').read()
    return a


Receiver = 'yash.gurukul12@gmail.com'
Receiver_Name = 'Yash'
Statement = '\n\nYour OTP -  ' + otp + '.'

mail.login('yash.gurukul12@gmail.com', Password())
mail.sendmail('yash.gurukul12@gmail.com', Receiver, 'Subject: Your OTP Mail... \n\nDear ' + Receiver_Name + Statement + '\n\nThanks\nYash Varshney\nV-C\n\nNote--This is a mail sent with Python Automation. \nIf You got this mail by mistake, please ignore')
mail.quit()
print('Sent Successfully.')
print("Congratulations")
