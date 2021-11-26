import  seaborn as sns
from pprint import pprint
import matplotlib.pyplot as plt
#Long-form Data
#Each variable is a column
#Each observation is a row

flights = sns.load_dataset("flights")
pprint(flights.head()) #Shows first few data point inside the flights table
sns.relplot(data=flights, x="year", y="passengers", hue="month", kind="line")
plt.show()
#Wide-form Data
#Try to study this a bit better
#Seaborn treats the argument to data as wide form when neither x nor y are assigned.

flights_wide = flights.pivot(index="year", columns="month", values="passengers")
pprint(flights_wide.head())
sns.relplot(data=flights_wide, kind="line")
plt.show()
sns.relplot(data=flights, x="month", y="passengers", hue="year", kind="line")
plt.show()

#to draw lines that represent the monthly time series for each year, simply reassign the variables
sns.relplot(data=flights, x="month", y="passengers", hue="year", kind="line")
plt.show()