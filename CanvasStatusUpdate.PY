# Webscrape to pull Canvas Status and report email updates
# Set up with System scheduler to run every 15 minutes indefinitely

# Libraries
import requests
import bs4
import smtplib
from email.message import EmailMessage
NOTI = []

# Get Request
url = 'https://status.instructure.com/'
r = requests.get(url)

# Email Push info from Work email to group
def email():
    gmail_user = "email"
    gmail_password = 'pass'

    sent_from = gmail_user
    to = [gmail_user" ]
    subject = "Check Instructure Status Page"
    body = "Status Change Indicated: http://status.instructure.com"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)  


    try:
        s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        s.ehlo()
        s.login(gmail_user, gmail_password)
        s.sendmail(sent_from, to, email_text)
        s.close()

    except:
        print('Something went wrong')

# Parse website
soup = bs4.BeautifulSoup(r.text, 'html.parser')

# Search for tags needed 
tags = soup.select('.status span')

# Search for string in tags and append to list
for x in tags:
    if "All Systems Operational" in str(x):
        NOTI.append(x)

# Verification of Operational Status
print(NOTI)

# If non operational run email
if "All Systems Operational" not in str(NOTI):
    print("Fail")
    email()
        
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
