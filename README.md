# Messaging Automation Script

This project provides a Python script and a shell script to send messages through various platforms including email, WhatsApp, Twitter, and SMS using the respective APIs.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Functionality](#functionality)
  - [send_messages.py](#send_messagespy)
  - [send_messages_curl.sh](#send_messages_curlsh)
- [Setup](#setup)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Required Python packages: `smtplib`, `pywhatkit`, `tweepy`, `twilio`
- cURL for running the shell script

You can install the required Python packages using pip:

```bash
pip install pywhatkit tweepy twilio
```

## Usage

### Python Script

You can run the Python script `send_messages.py` directly. It contains functions to send messages through various platforms.

### Shell Script

The shell script `send_messages_curl.sh` can be executed to send messages using cURL commands.

## Functionality

### send_messages.py

This Python script includes the following functions:

- **send_email(subject, body, to_email)**: Sends an email using SMTP.
- **send_whatsapp(phone_number, message)**: Sends a WhatsApp message using `pywhatkit`.
- **send_tweet(tweet_text)**: Sends a tweet using Tweepy.
- **send_sms(to_phone, message)**: Sends an SMS using Twilio.

#### Example Usage

To use the functions, you can modify the `__main__` section of the script as shown:

```python
if __name__ == "__main__":
    send_email("Test Subject", "Hello from Python!", "recipient@example.com")
    send_whatsapp("+1234567890", "Hello from WhatsApp!")
    send_tweet("Tweeting from Python!")
    send_sms("+09876543210", "Hello from SMS!")
```

### send_messages_curl.sh

This shell script sends messages using cURL commands:

- **Send email using SendGrid API**
- **Send WhatsApp message using Twilio API**
- **Send tweet using Twitter API**
- **Send SMS using Twilio API**

You can run the shell script directly in your terminal:

```bash
bash send_messages_curl.sh
```

## Setup

### Configuration

Before running the scripts, make sure to replace the placeholders with your actual credentials:

- In `send_messages.py`, update:
  - `your_email@example.com` and `your_password` with your email credentials.
  - `YOUR_CONSUMER_KEY`, `YOUR_CONSUMER_SECRET`, `YOUR_ACCESS_TOKEN`, and `YOUR_ACCESS_TOKEN_SECRET` with your Twitter API credentials.
  - `YOUR_ACCOUNT_SID` and `YOUR_AUTH_TOKEN` with your Twilio API credentials.

- In `send_messages_curl.sh`, update:
  - `YOUR_API_KEY`, `YOUR_ACCOUNT_SID`, `YOUR_AUTH_TOKEN`, and `YOUR_BEARER_TOKEN` with your respective API credentials.

## Conclusion

This project demonstrates how to automate messaging through various platforms using Python and cURL. You can extend the functionality or integrate more messaging services as needed.
