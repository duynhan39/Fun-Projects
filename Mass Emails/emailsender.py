import sys
#!/usr/bin/python

from string import Template

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


MY_ADDRESS = 'ps128@evansville.edu'
PASSWORD = 'Fazendeiro8!'

def get_contacts(info, idcode):
    names = []
    emails = []
    
    contacts_file = open(info, mode='r')
    contacts = contacts_file.readlines()
    id_file = open(idcode, mode='r')
    ids = id_file.readlines()
    
    for a_contact in contacts:
	#print (a_contact)
	#print (a_contact.split())
        names.append(a_contact.split()[0])
        emails.append(a_contact.split()[2])

    return names, emails, ids

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# set up the SMTP server
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

names, emails, ids = get_contacts('info.txt', 'code.txt')
message_template = read_template('content.txt')

print("Names: ", len(names))
print("Email: ", len(emails))
print("Codes: ", len(ids))

# For each contact, send the email:
count = 0
for name, email, idcode in zip(names, emails, ids):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title(), CODE=idcode.title())

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    #msg['To']='dc179@evansville.edu'
    msg['Subject']="Strengths Finder Access Code"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    count += 1
    del msg

print("Emails sent: ", count)

