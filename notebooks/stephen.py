import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt




df = pd.read_csv('Data/kc_house_data.csv')

# Count number of Null values 
#print(data.isna().sum())
# waterfront contains 2376 nulls
# view contains 63 nulls
# yr_renovated contains 3842 nulls

# Replace NaN values with Yes
df['waterfront'] = df['waterfront'].fillna('YES')
# Replace NaN values with 'Not rated'
df['view'] = df['view'].fillna('not rated')


# declaring X and Y values

x = df['price']
y = df['grade']

plt.bar(x, y)
plt.show()