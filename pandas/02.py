import pandas as pd
new_df = pd.read_csv('../workout_dataset.csv')

print(new_df.duplicated())