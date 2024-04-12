# How to add a Count Column to a Pandas DataFrame

import pandas as pd


df = pd.DataFrame({
    'experience': [5, 5, 2, 6, 6],
    'job': ['frontend', 'frontend', 'backend', 'tester', 'tester'],
})

print(df)

print('-' * 50)

df['job_count'] = df.groupby(['job'])['job'].transform('count')
print(df)