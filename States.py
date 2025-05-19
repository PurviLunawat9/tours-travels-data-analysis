#pd.read_csv() shows CSV file is imported in Python.

#dtf1.rename(column={},index={},inplace=True)shows that the column name to be changed and inplace =True means that the name of the column will be changed in original DataFrame.

#dtf1.loc[:5,:] shows the no.of visitors in 6 States of India and Abroad.

#dtf1[5:10:2] shows that extraction of data using slicing.

#dtf.iat[9,1]shows the visitors in Goa whereas dtf1.iat[4,3] shows the visitors in Australia.

#plt.subplot() is used for multiple views of line charts .

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Share of 10 States with no.of foreign tourists vists & Indian Departures.")
dtf1=pd.read_csv("H:\\purvi\\IP\\Tours & Travels\\States.csv")
print(dtf1)

print("                                                                                                                                                              ")
print("Changing the name of the column")
print(dtf1.rename(columns={"Number":"Foreign_Tourist_Arrivals"},inplace=True))
print(dtf1)


print("                                                                                                                                                              ")
print("No. of visitors in 6 States")
print(dtf1.loc[:5,:])


print("                                                                                                                                                              ")
print("Extracting data with random index no.")
print(dtf1[5:10:2])

print("                                                                                                                                                              ")
print("The minimum visitors in:")
print("Goa are:")
print(dtf1.iat[9,1])
print("Australia are:")
print(dtf1.iat[4,3])

print("                                                                                                                                                              ")
plt.figure(figsize=(10,7))

plt.subplot(2,1,1)
plt.plot(dtf1['States/UTs'],dtf1['Foreign_Tourist_Arrivals'],marker="o",markerfacecolor="black",linewidth=3,color="magenta")
plt.title("Tourism in India & in Foreign ")
plt.xlabel("India States/UT")
plt.ylabel("Foreign Tourist Arrivals")
plt.grid(True)
plt.subplots_adjust(hspace=0.4,wspace=0.4)


plt.subplot(2,1,2)
plt.plot(dtf1["ForeignStates"],dtf1["IndianDepartures"],marker="d",markerfacecolor='black',linewidth=5,color="orange")
plt.xlabel("Foreign States")
plt.ylabel("Indian Departures")
plt.grid(True)
plt.show()
