from twilio.rest import Client

client = Client(
    "ACd964ded0fc8ede45d1e4c81d31414eae", 
    "ccf4a9dea7fbf160f83cff08bc3b5ca4"
    )

for msg in client.messages.list():
    print(msg.body)
