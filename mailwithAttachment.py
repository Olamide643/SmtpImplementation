import smtplib                                       # Import the SMTPLIB Module
import os                                            # Importing OS Module
from email.mime.text import MIMEText                 # Import MimeText
from email.header import Header                      # Import Header
from email.mime.application import MIMEApplication   # Import MimeApplication 
from email.mime.multipart import MIMEMultipart       # Import MimeMultipart

receiver_email = 'adekoyaolamide643@gmail.com'       # Receiver Mail Address 

sender_email = os.environ["MAIL_USERNAME"]           # Sender mail address 

password = os.environ["MAIL_PASSWORD"]               # Sender Email Password

Subject = "Notification Mail"                        # Subject of the mail

mail = MIMEMultipart()                               

mail['Subject'] = Header(Subject,'utf-8').encode()
mail['From'] = sender_email
mail['To'] = receiver_email

with open('Message.txt') as f:                 # Open the html file and read content 
    raw_html = f.read()

        
content_of_msg  = MIMEText(raw_html,'html', 'utf-8')

mail.attach(content_of_msg)

path_to_files = r'C:\Users\olamide\Desktop\files'   # file path 

files  = os.listdir(path_to_files)

for file in files:
    with open(os.path.join(path_to_files,file), 'rb') as f:
        file_data = f.read()
        file_type= f.name.split(".")[-1]
        file_name = f.name
        attachedfile = MIMEApplication(file_data, _subtype = file_type)
        attachedfile.add_header(
                'content-disposition', 'attachment', filename=file )
    mail.attach(attachedfile)


    
try:
    smtp = smtplib.SMTP_SSL(host ='smtp.gmail.com') # Setup an SMTP Server over a secure connection
    smtp.login(sender_email,password)  #Login to the mail server  
    smtp.sendmail(sender_email,receiver_email,mail.as_string())   # Sending the mail out 
    print("Mail successfully sent")
    smtp.quit()
    smtp.close()
except Exception as e:
    print(f"Mail failed: Errror -> {e}")
    
    
