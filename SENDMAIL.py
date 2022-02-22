
import smtplib  # Import the SMTPLIB Module

import os       # Importing OS Module

receiver_email = 'adekoyaolamide643@gmail.com' # Reciever Mail Address 

sender_email = os.environ["MAIL_USERNAME"]  # Sender mail address 

password = os.environ["MAIL_PASSWORD"] # Sender Email Password

Subject = "Notification Mail" #Subject of the mail

customer_name = "CodeViber"

Body = """Hi {},\n
We are delighted to inform you that your request has been attended.
      \nThank you for choosing you.
      \nBest Regards,
      \ntesting@gmail.com""".format(customer_name)  # Body of the mail
       
Message = 'Subject: {} \n \n{}'.format(Subject,Body) # Message 


try:
    smtp = smtplib.SMTP_SSL(host ='smtp.gmail.com')    # Setup an SMTP Server 
    smtp.login(sender_email,password)  #  Login to the mail server  
    smtp.ehlo()                        #  Identify yourself to the connection
    smtp.sendmail(sender_email,receiver_email, Message)   # Sending the mail out 
    print("Mail successfully sent")
    smtp.quit()
    smtp.close()
except Exception as e:
    print(f"Mail failed: Errror -> {e}")



