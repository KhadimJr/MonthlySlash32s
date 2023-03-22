import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('uniqueS32sPerMonth', sep=" ", header=None, names=['Date','IPs'])
data.head(5)

group_data = data.groupby('Date')['IPs'].count()
plt.plot(group_data.index, group_data.values)
plt.xticks(np.arange(2012, 2023, 2))
plt.xlabel('Date')
plt.ylabel('Number of IPs')
plt.title('Distrubtions of /32 (2002-2022)')
plt.show()

data_date = data
data_date['Date'] = pd.to_datetime(data['Date'])
year_groups = data_date.groupby('Date')['IPs'].count()

plt.plot(year_groups.index, year_groups.values)
plt.xlabel('Date')
plt.ylabel('Number of IPs')
plt.title('Uniques /32 from 2002-2023')
plt.show()