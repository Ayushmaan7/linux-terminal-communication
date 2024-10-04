# Linux Terminal Communication

This repository provides scripts for sending messages through email, WhatsApp, Twitter, and SMS directly from the Linux terminal using Python and cURL. It aims to demonstrate the ease of communication via the command line.

## Overview

Two approaches are provided in this repository:

1. **Using Python Libraries** - A Python script that utilizes libraries like `smtplib`, `pywhatkit`, `tweepy`, and `twilio`.
2. **Using cURL with APIs** - A shell script that utilizes `cURL` to make HTTP requests to various APIs.

## Features

- Send Emails
- Send WhatsApp Messages
- Send Tweets
- Send SMS

## Getting Started

### Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `smtplib` (comes with Python)
  - `pywhatkit`
  - `tweepy`
  - `twilio`
- cURL (for the shell script)

You can install the required Python libraries using pip:

```bash
pip install pywhatkit tweepy twilio

