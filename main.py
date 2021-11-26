# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import pprint
import seaborn as sns
import matplotlib.pyplot as plt
#Why can't Pycharm fine the filepath the normal way? How will this affect it in deployment
#Ideally with datascience we do it on a notebook or shell cause frankly recompiling it is a waste time

pokemon = pd.read_csv("C:\\Users\\Azraf\\PycharmProjects\\SeabornKaggle\\Dataset\\Pokemon.csv")
print(pokemon.columns)
sns.histplot(data=pokemon, x="Type 1", multiple="stack")
plt.show()
sns.histplot(data=pokemon, x="Type 2", multiple="stack")
plt.show()
sns.histplot(data=pokemon, x="Type 1",y="Type 2", multiple="stack")
plt.show()



