# Hotel Room Booking System

## Overview

This is a simple Python-based hotel room booking system designed to demonstrate core programming concepts such as:
- user input handling
- conditional logic
- basic data storage using dictionaries
- data presentation with `pandas`
- QR code generation for payments using `qrcode`

The application allows a guest to select a room type, specify the length of stay, calculate the total cost, and generate a payment QR code.

## Features

- Four room categories with prices and available inventory:
  - `single bed` - ₹1500 per day
  - `double bed` - ₹2500 per day
  - `delux` - ₹4000 per day
  - `suite` - ₹5500 per day
- Accepts customer details: name, email, phone number
- Validates room availability before booking
- Calculates total amount automatically
- Generates a UPI payment QR code and opens it for easy payment

## Requirements

- Python 3.x
- `pandas`
- `qrcode`

Install dependencies with:

```bash
pip install pandas qrcode[pil]
```

## How to Run

From the project folder, execute:

```bash
python Room_booking_system.py
```

Follow the prompts to:
1. Enter your name
2. Enter your email address
3. Enter your phone number
4. Enter your room preference
5. Enter the number of days for your stay

If the chosen room is available, the script will display the booking amount and generate a QR code for payment.

## Notes for Recruiters

This project showcases the ability to build a functional command-line booking flow with:
- clear user interaction
- inventory management
- dynamic payment generation
- integration with third-party libraries
