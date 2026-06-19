import pandas as pd
import matplotlib.pyplot as plt

new_df = pd.read_csv('../workout_dataset.csv')

new_df.plot()
plt.show()
#dbsqlite