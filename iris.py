# importing the related packages.

import pandas as pd

data=pd.read_csv('employees.csv')

data.head()

data.shape

data.info()

# Data Preprocessing:

# identify and treating of Missing Values.

data.isnull().sum()

# data.dropna()

# Mean,Median--> filling of missing values.

# Dropping all the records of missing Values---> dropna().

# Check Duplicate records and  simply have the Unique records to be included into your dataset:

data[data.duplicated()]

# removing the Duplicate dataset.

data=data.drop_duplicates()

data.shape

data.head()

# Correlation Matrix

data.corr()

#- 1 to 1

# Positive Coreleation: relationship of Variable in Moving in Same direction

# Negative Corelation: relationship existing in inverse manner: one variable is increasing, other variable is decreasing.Vice-versa.

# No correlation or Zero : there is no existing relationship between the two variable.

# Data Visualization , analysing different features

ftr=['dept','numberOfProjects','timeSpent.company','workAccident','promotionInLast5years','salary']

ftr

import matplotlib.pyplot as plt
import seaborn as sns

fig=plt.subplots(figsize=(10,15))

for p,q in enumerate(ftr):
    plt.subplot(3,2,p+1)
    plt.subplots_adjust(hspace=1.0)
    sns.countplot(x=q,data=data, hue='left')
    plt.xticks(rotation=90)

# attrition rate: number of employee left/ number of total employees.

# Understanding

# People with low project as well as people with more number will have higher chance of churning out of the company.

# years of expierence: 3 - 6 years.

# Promotion---> significant role

# salary---> Low, Medium


# Conclusion:


# Promotion:Likely quit---> Havent  recieved promotion

# Time with Company: After 3 -6 year Crucial point the employee, affection with organisation.

# Number of project: if the opportunities are less or if the employee is over burdened , more chance of the employeee to quit the jobs.

# Salary : incentives based system to be introduced.

# Drill Report : Dash(web hosting), plotly

# Power BI, Tableau

# Model which help me to predict the churning out of the employee from the company .

data.head()

# Classification ---> Logistic Regression, Decision Tree Classifier, Random Forest Classsifier.
