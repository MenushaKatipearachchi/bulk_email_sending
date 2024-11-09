import os
import pandas as pd
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

data = pd.read_excel('email_list.xlsx')

# Looping through each row in the excel sheet
for index, row in data.iterrows():
    message = Mail(
        from_email=row['sender_email'],
        to_emails=row['recipient_email'],
        subject=row['subject'],
        html_content=row['message'])
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
