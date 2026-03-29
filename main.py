import requests
from datetime import datetime
import smtplib
#def is_near(a,b):
#    if (a>b and a-b<=5):
#        return True
#    elif (b>a and b-a<=5):
#        return True
#    else:
#        return False


MY_LAT = 19.054999 # Your latitude
MY_LONG = 72.8692035 # Your longitude

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASS"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour 

def is_near():
    if iss_latitude-5<=MY_LAT<=iss_latitude+5 and iss_longitude-5<=MY_LONG<=iss_longitude+5:
        return True
    else:
        return False
    

def is_dark():
    if time_now>sunset or time_now < sunrise:
        return True
    else:
        return False

if is_near and is_dark:
    connection = smtplib.SMPT("smpt.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr = MY_EMAIL,
        to_addrs = MY_EMAIL,
        msg = "Subject:look up\n\nThe iss is above u")
