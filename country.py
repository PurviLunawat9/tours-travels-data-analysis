#pd.read_csv() shows the CSV file that is imported in Python.

#df[“column name”] is used for adding a new column in the data frame.

#df.min() shows that which country least no.of tourists.

#df.iloc[0:9,]shows the top 9 countries with no.of tourists.

#df.sum() shows the total sum of FTA and IND 

#len(df.axes(0)) shows the no.of rows in a dataframe.

#plt.scatter() is used for scatter plot.

import pandas as pd
df=pd.read_csv('H:\\purvi\\IP\\Tours & Travels\\country table.csv')
print(df)
print("")
print("Adding a column IND :")
IND=[1938302,825565,77528,291605,315678,987542,94190,568073,1743261,1597707]
df["IND"]=IND
print(df)
print("")
print('Which country has minimum FTA and IND?')
print(df.min())
print("")
print('Print the top 9 countries with their FTA and IND')
print(df.iloc[0:9,:])
print("")
print('Print the total number of FTA and IND')
print(df.sum())
print("")
print('Printing total number of enrtries in each column')
print(len(df.axes[0]))

import matplotlib.pyplot as plt
print("")
country=df["COUNTRY"]
fta=df["FTA"]
ind=df["IND"]
plt.scatter(country,fta,marker='o',s=250,color='y',label='FOREIGN TOURIST AVAILABLE')
plt.scatter(country,ind,marker="*",s=250,color='b',label='INDIAN NATIONAL DEPARTURES')
plt.title("Country from Foreign Arrivals and Indian Departures")
plt.xlabel("Countries")
plt.ylabel("Tourists")
plt.grid(True)
plt.legend()
plt.show()

