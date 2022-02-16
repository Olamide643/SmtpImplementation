
import smtplib                  # Import the SMTPLIB Module
import os                       # Importing OS Module
from email.header import Header
from email.mime.text import MIMEText


receiver_email = 'adekoyaolamide643@gmail.com' # Reciever Mail Address 

sender_email = os.environ["MAIL_USERNAME"]     # Sender mail address 

password = os.environ["MAIL_PASSWORD"]         # Sender Email Password

Subject = "Notification Mail"                  #  Subject of the mail

with open('Message.txt') as f:                 # Open the html file and read content 
    raw_html = f.read()
    
        
msg = MIMEText(raw_html,'html', 'utf-8')

msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = Header(Subject,'utf-8').encode()

try:
    smtp = smtplib.SMTP_SSL(host ='smtp.gmail.com')              #  Setup an SMTP Server over a secure connection
    smtp.login(sender_email,password)                            #  Login to the mail server  
    smtp.ehlo()                                                  #  Identify yourself to the connection
    smtp.sendmail(sender_email,receiver_email,msg.as_string())   # Sending the mail out 
    print("Mail successfully sent")
    smtp.quit()
    smtp.close()
except Exception as e:
    print(f"Mail failed: Errror -> {e}")
                        
    