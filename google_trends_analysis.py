# Google Trends Keyword Analysis (Complete Project)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pytrends.request import TrendReq

# -------------------- STEP 1: Initialize PyTrends --------------------

pytrends = TrendReq(hl='en-US', tz=360)
keyword = 'Data Scientist'

# -------------------- STEP 2: Build Payload for Keyword --------------------

pytrends.build_payload([keyword], cat=0, geo='', gprop='', timeframe='today 12-m')

# -------------------- STEP 3: Regional Interest --------------------

region_data = pytrends.interest_by_region()
region_data = region_data.sort_values(by=keyword, ascending=False).head(15)

# --- Bar Plot: Regional Interest ---
plt.figure(figsize=(10, 6))
sns.barplot(x=region_data[keyword], y=region_data.index, palette='Blues_d')
plt.title(f'Search Interest by Region for "{keyword}"')
plt.xlabel('Search Interest')
plt.ylabel('Region')
plt.tight_layout()
plt.show()

# -------------------- STEP 4: Interest Over Time --------------------

time_df = pytrends.interest_over_time()

# --- Line Plot: Interest Over Time ---
plt.figure(figsize=(10, 6))
plt.plot(time_df.index, time_df[keyword], marker='o', color='red')
plt.title(f'Interest Over Time for "{keyword}"')
plt.xlabel('Date')
plt.ylabel('Interest')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------- STEP 5: Compare Multiple Keywords --------------------

kw_list = ['Data Scientist', 'Python Developer', 'Java Developer']
pytrends.build_payload(kw_list, cat=0, geo='', gprop='', timeframe='today 12-m')
compare_df = pytrends.interest_over_time()

# --- Line Plot: Keyword Comparison ---
plt.figure(figsize=(10, 6))
for kw in kw_list:
    plt.plot(compare_df.index, compare_df[kw], label=kw)

plt.title('Keyword Comparison Over Time')
plt.xlabel('Date')
plt.ylabel('Interest')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------- STEP 6: City-wise Interest --------------------

city_wise = pytrends.interest_by_region(resolution='CITY')
city_wise = city_wise.sort_values(by=keyword, ascending=False).head(15)

# --- Bar Plot: Interest by City ---
plt.figure(figsize=(10, 6))
plt.barh(y=city_wise.index, width=city_wise[keyword], color='green')
plt.title(f'Search Interest by City for "{keyword}"')
plt.xlabel('Search Interest')
plt.ylabel('City')
plt.grid(axis='x')
plt.tight_layout()
plt.show()
