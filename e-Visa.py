#pd.read_csv(index_col=’’) shows the CSV file imported in Pyton and index_col is used for making the column as the index of the DataFrame.

#dtf.loc[:,0:2].isnull() shows how many Visas were issued in 2019 and 2020.

#dtf.count() shows the no. times Visas were issued in 2019 and 2020.

#plt.bar() is used to plot bar graph.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print("Month-wise arrival of Foreign Tourist availing e-Visas")
dtf3=pd.read_csv("H:\\purvi\\IP\\Tours & Travels\\e-Visa.csv")
print(dtf3)

print("                                                                                                                                                              ")
dtf=pd.read_csv("H:\\purvi\\IP\\e-Visa.csv",index_col="Month")
print("No issue of e-visas in 2019 and 2020")
a=dtf.iloc[:,0:2].isnull()
print(a)

print("                                                                                                                                                              ")
print("No.of times e-Visas were issued in 2019 and 2020")
print(dtf.count())

print("                                                                                                                                                              ")
print("")
plt.figure(figsize=(10,7))
x=np.arange(len(dtf3["Month"]))
plt.bar(x,dtf3.Year2019,width=0.45,color="cyan",label=2019)
plt.bar(x+0.45,dtf3.Year2020,width=0.45,color="orange",label=2020)
plt.xticks(x,dtf3["Month"])
plt.xlabel("Months")
plt.ylabel("e-Visa Issues")
plt.title("Foreign Tourists availing e-Visa")
plt.legend()
plt.show()
