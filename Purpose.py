#FTA-Foreign Tourist Arrivals

#IND-Indian National Departures

#pd.read_csv() means that CSV file imported into the Python.

#df.max() shows the maximum purpose for the visit.

#df[“FTA”] shows the values in the column FTA.

#df.tail(4) shows the last 4 rows of Purpose Table.

#df.iloc[3:6,0:3] shows the middle rows of the Purpose Table.

#plt.barh() represents horizontal bar, in this table multiple bars is plotted using width, yticks(), color, label, legend.

import pandas as pd
import numpy as np
df=pd.read_csv('H:\\purvi\\IP\\Tours & Travels\\purpose table.csv')
print(df)
print('')
print('For which purpose the tourists have travelled the maximum')
print(df.max())
print('')
print('Print all the values in the column FTA')
s=df["FTA"]
print(s)
print('')
print('Print any 4 purposes with FTA nd IND')
print(df.tail(4))
print('')
print('Print any 3 purposes from the middle')
print(df.iloc[3:6,0:3])
print('')

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
purpose=df["PURPOSE"]
fta=df["FTA"]
ind=df['IND']
obj=np.arange(len(purpose))
width=0.45
plt.yticks(obj,purpose)
plt.barh(obj,fta,width,color='r',label='Foriegn Tourist Arrivals',align="center")
plt.barh(obj+width,ind,width,color='y',label='Indian Tourist Departments',align="center")
plt.title("Purpose for Tourism to India & Abroad")
plt.legend()
plt.show()
