# Install Twilio packgage
from twilio.rest import Client

# Input SID and Authorize token here
client = Client(
    "TWILIO_ACCOUNT_SID", 
    "TWILIO_AUTH_TOKEN"
    )

# Sending message
message = client.messages.create(
    from_="+16065311900",
    to="+12067246799",
    body="Hello World from Python",
    )

# Deleting message
#for message in client.messages.list():
#    print(f"Deleting {message.sid}")
#    message.delete()

print(f"Created a new message: {message.sid}")
