# MAKE SURE THAT YOUR GMAIL CAN BE ACCESSED BY LESS SECURE APPS.
# YOU CAN TURN IT ON YOUR SETTINGS.

import smtplib
from  email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
from  email.mime.base import MIMEBase
from  email import encoders 

#------------------- CONNECTING & LOGIN TO MAIL --------------------

user_email='@gmail.com'                 # ENTER YOUR EMAIL ADDRESS
user_password=''                        # ENTER YOUR EMAIL PASSWORD
TO_email='@gmail.com'                   # ENTER 'TO' EMAIL ADDRESS
                                        # YOU CAN FILL THE CONTENT OF 'SUBJECT',
                                        # EMAIL BODY AS YOU WISH.
subject_contnet='Email sending using python'
email_body='Hey  , this is a message sent by using python.\nHow was today!\nDid you find any class intresting today! . ' 


msg = MIMEMultipart()
msg['From']= user_email
msg['To']= sender_email
msg['Subject']= subject_contnet

#------------------- ADDING FROM & TO  ADDRESS OF THE MAIL AND ALSO 'SUBJECT' --------------------

msg.attach(MIMEText(email_body,'plain'))

filename= "workfile.txt"         # YOU CAN ATTACH ANY FILES THAT PRESENT IN YOUR
attachment= open(filename,"rb")     # CURRENT WORKING DIRECTORY WHERE THIS PROGRAM SAVED.

part=MIMEBase('application','octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text=msg.as_string()

#------------------- connecting to server ----------------------------

server=smtplib.SMTP('smtp.gmail.com',587)# To connect the SMTP SERVER which is used by the GOOGLE.
server.ehlo()
server.starttls() # TLS = Transport Layer Security Which starts encoding.
server.login(user_email,user_password)

#------------------- SENDING EMAIL ----------------------------------
server.sendmail(user_email,TO_email,text)

#------------------- quitting fron server ----------------------------

server.quit()


