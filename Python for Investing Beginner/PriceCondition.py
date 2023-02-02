import pandas as pd
import numpy as np
from ImportAndExportData import ImportDataFromYahoo

df = ImportDataFromYahoo('coin','BTC-USD', '2021-01-01', '2022-05-01')
df['Return'] = df['Close'].pct_change()

#Filter ราคาปิดที่มีค่ามากกว่า 60,000 USD
# print(df[df.Close > 60000])

#Filter Return ที่มีค่ามากกว่า 0
# print(df[df['Return'] > 0])

#สร้าง Function แล้วให้ Print โดยมี Condition ที่ว่าหาก Return > 0 ให้ Print "Gain" หาก Return < 0 ให้ปริ้น "Loss"
df['Return_Condition'] = np.where(df['Return'] < 0,  "Loss", "Gain")
sum_loss = len(df[df['Return'] < 0])
sum_gain = len(df[df['Return'] > 0])
sum_len = len(df)
percent_loss = (sum_loss/sum_len *100)
percent_gain = (sum_gain/sum_len *100)

print("Number of expected loss are {0} times in {1} about {2:.2f}%".format(sum_loss, sum_len, percent_loss))
print('Number of expected gain are {0} times in {1} about {2:.2f}%'.format(sum_gain, sum_len, percent_gain))
