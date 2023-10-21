from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid 
from fastapi.middleware.cors import CORSMiddleware

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

blockchain = [
    {'skey': 'abc-123','uid': '999941057058', 'name': 'Shivshankar Choudhury', 'visitdate': '13-05-1968', 'symp': 'birth' ,'diag': 'good', 'pres': 'nothing'},
]

        
app = FastAPI()

origins = ["http://127.0.0.1:5500"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AuthJSON(BaseModel):
    uid : str
    name : str
    otp : int
    

class GetPres(BaseModel):
    uid  : str
    skey : str
    
class PresJSON(BaseModel):
    skey : str
    uid  : str
    name : str
    pres : str
    diag : str
    vdate : str

@app.post("/createpres/")
async def auth(create: PresJSON):
    try:
        new_entry = {'skey': create.skey, 'uid': create.uid, 'name': create.uid, 'visitdate': create.vdate, 'diag': create.diag, 'pres': create.pres}
        blockchain.append(new_entry)
        return {"skey": create.skey, "isertion": "y"}
    except:
        return {"skey": create.skey, "isertion": "n"}
    
@app.post("/getpres/")
async def auth(fetch: GetPres):
    records = []
    for item in reversed(blockchain):
        if (item.get('uid') == str(fetch.uid)):
                new_entry = {'skey': item.get('skey'), 'visitdate': item.get('visitdate'), 'pres': item.get('pres'), 'name': item.get('name'), 'symp': item.get('symp'), 'diag': item.get('diag')}
                records.append(new_entry)
    return {"data": records}

    
@app.post("/auth/")
async def auth(auth: AuthJSON):
    # skey = 13255
    skey = (uuid.uuid1()) 
    print(skey)
    for item in db:
        if ((item.get('uid') == str(auth.uid)) & (item.get('name') == str(auth.name))):
            return {"skey": skey, "auth": "y"}
    return {"skey": skey,"auth":"n"}