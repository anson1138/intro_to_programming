from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC77b5053ae6141844d769ec06b2a51688"
AUTH_TOKEN = "b9ac6181bd150d1c2733844d363e4f7f"
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
  
message = client.sms.messages.create(
      to="+16506787769",
      from_="+16504379446",
      body="Hi this is me testing this twilio thing for Udacity python training",
      media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg", 
)

print message.sid
