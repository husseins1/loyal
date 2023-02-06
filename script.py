from twilio.rest import Client 
 
account_sid = 'ACc27bb9e9b7a2007fd5e2f5b7116b5dad' 
auth_token = '[Redacted]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:+9647806969277' 
                          ) 
 
print(message.sid)