from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Test Database for Aadhar auth
db = [
    {'uid': '999941057058', 'name': 'Shivshankar Choudhury', 'dob': '13-05-1968', 'dobt': 'V', 'gender': 'M',
     'phone': '2810806979', 'email': 'sschoudhury@dummyemail.com', 'street': '12 Maulana Azad Marg', 'vtc': 'New Delhi',
     'subdist': 'New Delhi', 'district': 'New Delhi', 'state': 'New Delhi', 'pincode': '110002'},
    {'uid': '999971658847', 'name': 'Kumar Agarwal', 'dob': '04-05-1978', 'dobt': 'A', 'gender': 'M',
     'phone': '2314475929', 'email': 'kma@mailserver.com', 'building': 'IPP, IAP', 'landmark': 'Opp RSEB Window',
     'street': '5A Madhuban', 'locality': 'Veera Desai Road', 'vtc': 'Udaipur', 'district': 'Udaipur',
     'state': 'Rajasthan', 'pincode': '313001'},
    {'uid': '999933119405', 'name': 'Fatima Bedi', 'dob': '30-07-1943', 'dobt': 'A', 'gender': 'F',
     'phone': '2837032088', 'email': 'bedi2020@mailserver.com', 'building': 'K-3A Rampur Garden', 'vtc': 'Bareilly',
     'district': 'Bareilly', 'state': 'Uttar Pradesh', 'pincode': '243001'},
    {'uid': '999955183433', 'name': 'Rohit Pandey', 'dob': '08-07-1985', 'dobt': 'A', 'gender': 'M',
     'phone': '2821096353', 'email': 'rpandey@mailserver.com', 'building': '603/4 Vindyachal',
     'street': '7TH Road Raja Wadi', 'locality': 'Neelkanth Valley', 'poname': 'Ghatkopar (EAST)', 'vtc': 'Mumbai',
     'district': 'Mumbai', 'state': 'Maharashtra', 'pincode': '243001'},
    {'uid': '999990501894', 'name': 'Anisha Jay Kapoor', 'gender': 'F', 'dob': '01-01-1982', 'dobt': 'V',
     'building': '2B 203', 'street': '14 Main Road', 'locality': 'Jayanagar', 'district': 'Bangalore',
     'state': 'Karnataka', 'pincode': '560036'}
]
otp = 420690

#Initializing FastAPI as app
app = FastAPI()

#defining how the input of json will look like
class AuthJSON(BaseModel):
    uid : int
    name : str
    otp : int
    skey : int
    

# Defining what the post request will do
@app.post("/2.5/")
async def auth(auth: AuthJSON):
    for item in db:
        if ((item.get('uid') == str(auth.uid)) & (item.get('name') == str(auth.name)) & (otp == auth.otp)):
            return {"skey": auth.skey, "auth": "y"}
        else:
            return {"skey": auth.skey, "auth": "n"}