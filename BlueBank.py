# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 08:01:01 2022

@author: Mazadur Rahman
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# method 1 to read json data file

json_file = open('loan_data_json.json')    # open json file
data = json.load(json_file)                # read json file

# method 2 to read json data file
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    

# transform to datafram
#df_name = pd.DataFrame(data) <------- Formula
#df =datafram   & pd = pandas

loandata = pd.DataFrame(data)

# finding unique values for purpose column 
loandata['purpose'].unique()

# finding unique value with groupby function
purposecount = loandata.groupby(['purpose']).size()

# describe the data
loandata.describe()

#discribe the data for a specific column
loandata['int.rate'].describe()
loandata['purpose'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# using EXP() to get annual income
income = np.exp(loandata['log.annual.inc'])  # extract data
loandata['annualincome'] = income            # add new data

# playing with array
# Befor playing array we must have to import NumPy laibary
# 0D Array
arr = np.array(1090)

# 1D Array
arr = np.array([1, 2, 3, 4])

# 2D Array 
arr = np.array([[1, 2, 3, 4] , [4, 5, 6, 7]])

# Working with IF Statements

a = 10
b = 90

if b > a:
    print(' b is greater then a')
    
# lets add more condition 

a = 10
b = 90 
c = 1090

if b > a and b < c:
    print(' b is greater then a and less then c')

# what if a condition is not met

a = 10
b = 90 
c = 9

if b > a and b < c:
    print(' b is greater then a and less then c')
else:
    print(' No condition met')

# another condition different metrics

a = 10
b = 90 
c = 9

if b > a and b < c:
    print(' b is greater then a and less then c')
elif b > a and b > c:
    print(' b is greater then a and c')
else:
    print(' No condition met')


# FICO Score

fico = 700

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 600 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
    
print(ficocat)

# For loops

fruit = ['banana', 'mango', 'jackfruit', 'papaya']

for x in fruit:
    print(x)
    y = x + ' native fruits'
    print(y)

for x in range(0,4):
    y = fruit[x]+ ' for sale'
    print(y)

 
# applying forloops to loan data
# for only fist 10 rows

ficocat10 = []
for x in range(0,10):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 600 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat10.append(cat)
        

# for holl data set

length = len(loandata)   # find length of particular column
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Error - Unknown'
    ficocat.append(cat)
        

ficocat = pd.Series(ficocat)  # convart list to series 

loandata['fico.category'] = ficocat   # add new column in old datafram


#df.loc as conditional statements
# df.loc[df['ColumnName'] condition, NewColumnName] = 'value if condition met'

# for interest rates, a new column is wanted.  rate > 0.12 then high else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'



# using python code to make chart/plot
# befor creat chart we have to import matplotlib.pyplot laibary

# number of loans/rows by fico.category
# groupby function
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green' , width = 0.7)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'orange' , width = 0.4)
plt.show()

# scatter plots
xpoint = loandata['dti']
ypoint = loandata['annualincome']
plt.scatter(xpoint, ypoint, color = '#87CEEB')
plt.show()


# writing to CSV /output clean data
loandata.to_csv('loan cleaned.csv', index = True)













