import pandas as pd
import qrcode
import os


Rooms={
    'single bed':{'price':1500,'available':12},
    'double bed':{'price':2500,'available':8},
    'delux':{'price':4000,'available':9},
    'suite':{'price':5500,'available':8}
}

d=pd.DataFrame(Rooms)

print("Welcome to Ganga hotel🏩")
name=input("Enter ur name; ")
email_id=input("Enter ur email id: ")
phone=int(input("Enter ur phone number: "))
customer_room=input("Enter ur room prefrence: ").lower()
if customer_room in Rooms and Rooms[customer_room]['available'] > 0:
    days=int(input("Enter ur days for stay: "))
    amount=Rooms[customer_room]['price']*days
    print(F"Your total amount of stay {days} days in {customer_room} room is ₹{amount} ")
    Rooms[customer_room]['available']-=1

    upi_id="9315601379-1@ybl"
    name="kavyasingh"
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"
    qr=qrcode.make(upi_link)
    qr.save("test_qr.png")
    os.startfile("test_qr.png")
    print(f"Please scan the qr code for ur payment of ₹{amount}")
else:
    print(f"Your preferd room {customer_room} is currently not ❌ available in our hotel")




