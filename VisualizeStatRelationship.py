import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid") #Seaborn actually provides a lot of themes like d3.js
                                #Unlike D3 they are built in so we can just set them
                                #Look into these

tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips);
plt.show() #This is because we practicing from an IDE. In a Python notebook, jupyter or Collab this won't be neccesary
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips);
plt.show()

#We can use different markers to better visualize the plot
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker",data=tips)
plt.show()

#We can add qualitative palette  to better visualize our data. Here we see some are deeper but I am not sure why.
#Tutorial doesn't explain that well

sns.relplot(x="total_bill", y="tip", hue="size", data=tips)
plt.show()

#Line Plots can be used to demonstrate importance of continuity in the data.

df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
g.figure.autofmt_xdate()
plt.show()
