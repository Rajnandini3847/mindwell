import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = "e8e6fb61"
VONAGE_API_SECRET = "7NCsDAIv5fAUFjLV"
VONAGE_BRAND_NAME = "akash"
TO_NUMBER = "916201933790"

import vonage

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

responseData = client.sms.send_message(
    {
        "from": VONAGE_BRAND_NAME,
        "to": TO_NUMBER,
        "text": "A text message sent using the Vonage SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")