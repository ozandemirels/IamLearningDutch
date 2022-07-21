import time
import pandas as pd
import pywhatkit
from datetime import datetime
from random import randint


file_loc = 'C:/Users/ozan.demirel/PycharmProjects/IamLearningDutch/Dutch.xlsx'
df = pd.read_excel(file_loc, index_col=None, na_values=['NA'])
listLength = len(df.index)


while True:
    today = str(datetime.now())
    hourNow = int(today[11:13])
    minuteNow = int(today[14:16])
    if minuteNow == 59 and hourNow > 7 and hourNow < 23:
        randomNumber = randint(0, listLength - 1)
        pywhatkit.sendwhatmsg('+905322807393', ( 'Dutch : ' + df.iloc[randomNumber, 0] + '\n' + 'Pronunciaton : ' + df.iloc[randomNumber, 1] + '\n' + 'English : ' + df.iloc[randomNumber, 2]), hourNow+1, 0)
        time.sleep(60*59)






