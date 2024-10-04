#!/bin/bash

# Send email using cURL
curl -X POST "https://api.sendgrid.com/v3/mail/send" \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{
    "personalizations": [{"to": [{"email": "recipient@example.com"}]}],
    "from": {"email": "your_email@example.com"},
    "subject": "Test Subject",
    "content": [{"type": "text/plain", "value": "Hello from cURL!"}]
}'

# Send WhatsApp message using Twilio
curl -X POST "https://api.twilio.com/2010-04-01/Accounts/YOUR_ACCOUNT_SID/Messages.json" \
--data-urlencode "To=whatsapp:+1234567890" \
--data-urlencode "From=whatsapp:+14155238886" \
--data-urlencode "Body=Hello from cURL!" \
-u YOUR_ACCOUNT_SID:YOUR_AUTH_TOKEN

# Send tweet using cURL
curl -X POST "https://api.twitter.com/2/tweets" \
-H "Authorization: Bearer YOUR_BEARER_TOKEN" \
-H "Content-Type: application/json" \
-d '{"text":"Tweeting from cURL!"}'

# Send SMS using Twilio
curl -X POST "https://api.twilio.com/2010-04-01/Accounts/YOUR_ACCOUNT_SID/Messages.json" \
--data-urlencode "To=+09876543210" \
--data-urlencode "From=+1234567890" \
--data-urlencode "Body=Hello from cURL!" \
-u YOUR_ACCOUNT_SID:YOUR_AUTH_TOKEN
