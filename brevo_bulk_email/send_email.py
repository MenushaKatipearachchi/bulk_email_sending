import pandas as pd
import requests
import json

# Load the Excel file
df = pd.read_excel("email_list.xlsx")

# Headers
headers = {
    "accept": "application/json",
    "api-key": "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"
}

# URL
url = "https://api.brevo.com/v3/smtp/email"

# Iterate over each row in the excel file
for index, row in df.iterrows():
    body = {
        "sender": {
            "email": row["sender_email"],
            "name": row["sender_name"]
        },
        "subject": "Default Subject Line",
        "htmlContent": "<h1>Default Heading</h1><p>Default paragraph.</p>",
        "messageVersions": [
            {
                "to": [
                    {
                        "email": row["recipient_email"],
                        "name": row["recipient_name"]
                    }
                ],
                "htmlContent": row["message"],
                "subject": row["subject"]
            }
        ]
    }

    # POST request
    response = requests.post(url, headers=headers, data=json.dumps(body))

    print(f"Email sent to {row['recipient_email']}. Response status code: {response.status_code}")
