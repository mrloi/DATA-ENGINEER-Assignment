#Task1:
#dataset : https://archive.ics.uci.edu/static/public/849/power+consumption+of+tetouan+city.zip
#!pip3 install pandas
import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("Tetuan City power consumption.csv")
df
df.info()

#Task2:
#Cleaning and transform data
#Eliminate duplicate data
df['is_duplicate'] = df.duplicated()
df = df[df['is_duplicate'] == False]
df = df.drop(columns=['is_duplicate'])

#Check if data is missing or not
df.isnull()
df.isnull().values.any()


#Check and handle outliers data (outliers)
# Tính toán phạm vi IQR cho từng trường
df = df.drop('DateTime', axis=1)  

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Identify outliers for each field
outliers = (df < Q1 - 1.5 * IQR) | (df > Q3 + 1.5 * IQR)

outliers
outlier_count = outliers.sum()

print("Số lượng dữ liệu ngoại lai cho từng trường:")
print(outlier_count)

#Generate summary statistics for three key variables
df[['Temperature', 'Humidity', 'Wind Speed']].describe()

