import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_data.csv")

df.plot()
plt.savefig("results/plot1.png")

df.hist()
plt.savefig("results/plot2.png")

print("Visualization completed")