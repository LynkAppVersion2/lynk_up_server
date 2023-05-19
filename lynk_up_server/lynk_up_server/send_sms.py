# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = 'AC78acde7f808ca3f69b2b85560db44155'
auth_token = '1351b1e47934846893c9e9c4c9a69388'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         messaging_service_sid='MG9752274e9e519418a7406176694466fa',
         body='body',
         to='+18327294919'
     )

print(message.sid)

