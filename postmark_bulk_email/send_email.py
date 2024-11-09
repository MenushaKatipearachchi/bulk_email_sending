import pandas as pd
from postmarker.core import PostmarkClient

def send_email(server_token, from_email, to_email, subject, message):
    client = PostmarkClient(server_token=server_token)
    email = client.emails.Email(
        From=from_email,
        To=to_email,
        Subject=subject,
        HtmlBody=message
    )
    response = email.send()
    return response

server_token = 'a2fdeb5e-68a1-4644-9715-a3bd653e929a'

# Read the Excel file
data = pd.read_excel('email_list.xlsx')

# Loop through each row in the DataFrame
for index, row in data.iterrows():
    from_email = row['sender_email']
    to_email = row['recipient_email']
    subject = row['subject']
    message = row['message']

    # Send the email
    send_email(server_token, from_email, to_email, subject, message)

