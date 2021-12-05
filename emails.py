#!/usr/bin/env python3

import email.message
import mimetypes
import os
import smtplib
import getpass
import sys

def generate(sender, recipient, subject):
    """Creates an email with an attachment."""
    #Basic Email formatting
    message=email.message.EmailMessage()
    message['From']=sender
    message['To']=recipient
    message['Subject']=subject
    #Here Subject would depend upon the type of error and will be initialised on the time of error identification
    message.set_content("Please check your system and resolve the issue as soon as possible.")
    return message

def send(message):
    """Sends message to the administrator informing about the error."""
    uname=os.getlogin()
    path='/home/'+uname+'/mail-config-pass.txt'
    with open(path) as f:
        for line in f:
            mail_password=line
    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.set_debuglevel(1) #To get processing information(run in debug mode)
        smtp.starttls()
        #mail_pass=getpass.getpass("Password?") #uncomment this statement to enter password at time of execution of script
        #default prompt is 'password' for getpass method
        smtp.login(message['From'], mail_password.strip()) #NOTE:here password is in plain context
        #To use password in more secure way, use getpass module
        smtp.send_message(message)
    print('message sent successfully from {} to {}'.format(message['From'], message['To']))
