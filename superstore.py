import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('data/Sample - Superstore.csv', encoding='latin1', encoding_errors='ignore')


# df.info()

print(df.isna().sum())

# SALES BY REGION (pie chart)
region_sales = data.groupby('Region')['Sales'].sum()

# SALES BY REGION
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%')
plt.title("sales by region")
plt.show()



# 1.Regional Analysis

#利润率
# df['Profit Margin'] = df['Profit'] / df['Sales']
# df['Cost']=df['Sales']-df['Profit']
# df['profit_margin']=(df['Profit']/df['Sales'])*100

