# importing python libraries
from datetime import datetime
from pytz import timezone
import requests

# how to get date and time of EST
tz = timezone('America/New_York')
now = datetime.now(tz)
dt_string = now.strftime("%d/%m/%Y" + " at " + "%H:%M:%S")

# how to get bitcoin price
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
bitcoin_price = data['bpi']['USD']['rate']

# opening a file and writing the information
file1 = open("info.txt", "a")
file1.write(
    str(f"Bitcoin\'s current price on {dt_string}: ${bitcoin_price} \n \n"))
file1.close()

# making sure the code works properly and runs all the way through
print("done!")
