#pd.read_csv() shows the CSV file that is imported in Python.

#dt.min() shows minimum visitor in 2019 and 2020.

#dt.Year2019+dt.Year2020 means combining both the columns where there is no value then it will give NaN.

#plt.scatter() for scatter chart and plt.plot() for line chart.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Month-wise Foreign Tourist Arrivals in India")
dt=pd.read_csv("H:\\purvi\\IP\\Tours & Travels\\Month.csv")
print(dt)

print("                                                                                                                                                             ")
print("Minimum visitors in 2019 and 2020.")
print(dt.min())

print("                                                                                                                                                             ")
print("Combinig 2019 and 2020")
print(dt.Year2019+dt.Year2020)

print("                                                                                                                                                             ")
plt.figure(figsize=(10,7))
x=np.arange(len(dt["Month"]))
plt.plot(x,dt.Year2019,linewidth=5,label=2019)
plt.scatter(x,dt.Year2020,color="red",marker='^',s=150,label=2020)
plt.xticks(x,dt["Month"])
plt.xlabel("Months")
plt.ylabel("Foreign Tourists ")
plt.title("Foreign Tourists Arrivals in India")
plt.legend()
plt.grid(True)
plt.show()
