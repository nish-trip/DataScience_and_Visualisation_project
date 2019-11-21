import pandas as pd 
import numpy as np 
import unicodecsv as u 
import matplotlib.pyplot as m
import seaborn as sns


#Function to convert the data type from string to integer for specific columns
def fix_types(df):
	df[['Age','Market_value','Transfer_fee']]=df[['Age','Market_value','Transfer_fee']].apply(pd.to_numeric)

#Function to find the number of missing values in each column
def no_of_missing(df):
    print(df.isnull().sum())


#Function to fill missing values with median
def fill_missing(df):
    df.fillna(df.median(),inplace=True)


#reading csv file
df =pd.read_csv('/Users/apple/Documents/IDS_project/top250-00-19.csv')

#printing first 5 rows of dataset
print(df.head())

#printing datatypes after fixing
fix_types(df)
print(df.dtypes)

#printing number of missing values in each column - 76 in 'Market_value' column
no_of_missing(df)

#printing number of missing values after filling with median - 0 in 'Market_value' column
fill_missing(df)
no_of_missing(df)


#writing cleaned dataframe to new csv file
df.to_csv('/Users/apple/Documents/IDS_project/cleaned_dataset.csv')














   

                                                








