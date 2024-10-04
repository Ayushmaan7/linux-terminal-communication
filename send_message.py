# send_messages.py
import smtplib
import pywhatkit as kit
import tweepy
from twilio.rest import Client

# Function to send an email
def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    password = "your_password"

    msg = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg)

# Function to send a WhatsApp message
def send_whatsapp(phone_number, message):
    kit.sendwhatmsg(phone_number, message, 15, 0)

# Function to send a tweet
def send_tweet(tweet_text):
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(tweet_text)

# Function to send an SMS
def send_sms(to_phone, message):
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_='+1234567890', to=to_phone)

# Example usage
if __name__ == "__main__":
    send_email("Test Subject", "Hello from Python!", "recipient@example.com")
    send_whatsapp("+1234567890", "Hello from WhatsApp!")
    send_tweet("Tweeting from Python!")
    send_sms("+09876543210", "Hello from SMS!")
