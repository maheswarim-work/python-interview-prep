import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data5.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()
