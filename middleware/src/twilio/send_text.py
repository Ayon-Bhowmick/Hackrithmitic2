# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

def send_text_msg(destination: str , msg: str):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body= msg,
            from_='+19096711856',
            to=destination
        )

    print(message.sid)


def main():
    send_text_msg('6017918060',"Testing 4: GO!! TO SLEEP SMH")
    
if __name__=="__main__":
    main()
