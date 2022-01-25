from twilio.rest import Client

client = Client(
    "TWILIO_ACCOUNT_SID", 
    "TWILIO_AUTH_TOKEN"
    )

message = client.messages.create(
    from_="+16065311900",
    to="+12067246799",
    body="Hello World!",
    )

print(message.sid)
