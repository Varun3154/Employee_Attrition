#!/usr/bin/env python
# coding: utf-8

# ## Employee Attrition Rate

# #### Importing libraries

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #### Data Importing
# Read() csv file ! ,
# head function - Show Top 5 Entry your csv file

# In[4]:


df = pd.read_csv("Employee-Attrition.csv")


# In[5]:


df.head()


# #### Data processing
# columns fun. - Show All Columns In Your CSV File
# Shap fun. -  returns the shape of an array
# unique    - show unique value in csv file

# In[6]:


df.columns


# In[7]:


df.shape


# In[8]:


df["Department"].unique


# In[9]:


df.info()


# In[10]:


df.describe().style.background_gradient()


# #### EDA - using matplotlib

# In matplotlib we have multiple kinds of graphs including:
# * Bar Graph
# * Pie Chart
# * Box Plot
# * Histogram
# * Line Chart and Subplots
# * Scatter Plot

# #### convert string to integer
# map() - convert string to integer

# #### Bar Graph

# In[11]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = df["Attrition"]
y = df["Age"]
plt.xlabel('Attrition') 
plt.ylabel('Age') 

plt.title("Bar graph of Age and attrition")
ax.bar(x,y, color='green')
plt.show()


# This is Bar Graph who is define Attrition or Age Value.

# This bar graph here is describing the values of department and education column where the education level of each department is max 5.

# In[12]:


df['Attrition'] = df['Attrition'].map({'Yes':1, 'No':0})


# In[13]:


df.head()


# In[46]:


df['Education'].replace([1,2,3,4,5],['BelowCollege','College','Bachelor','Master','Doctor'], inplace=True)
df['EnvironmentSatisfaction'].replace([1,2,3,4],['Low', 'Medium','High','VeryHigh'],inplace=True)
df['JobInvolvement'].replace([1,2,3,4],['Low', 'Medium', 'High', 'VeryHigh'], inplace=True)
df['JobSatisfaction'].replace([1,2,3,4],['Low', 'Medium', 'High', 'VeryHigh',], inplace=True)
df['PerformanceRating'].replace([1,2,3,4,],['Low', 'Good', 'Excellent', 'Outstanding'], inplace=True)
df['RelationshipSatisfaction'].replace([1,2,3,4],['Low', 'Medium', 'High', 'VeryHigh',], inplace=True)
df['WorkLifeBalance'].replace([1,2,3,4],['Bad','Good','Batter','Best',], inplace=True)


# In[47]:


df.head()


# In[16]:


df.info()


# In[17]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = df["Department"]
y = df["EmployeeCount"]
plt.xlabel('EmployeeCount') 
plt.ylabel('Department') 

plt.title("Bar graph of Age and attrition")
ax.bar(x,y, color='blue')
plt.show()


# The bar Graph is Show Deaprtment Value.
# There are 3 type of Department 
# * Sales
# * Research & Development
# * human resource

# #### stack bar chart

# In[18]:


X = df['DistanceFromHome']
Y = df['EmployeeNumber']
colors = ['r', 'g',]
# plt.bar(X, Y, color=colors,width=0.5,)
df.plot(x='DistanceFromHome', kind='bar', stacked=True,color=colors)
plt.title("Stack Bar graph")
plt.xlabel("DistanceFromHome")
plt.ylabel("EmployeeNumber")
plt.show()


# In[19]:


df.head()


# In[20]:


fig,ax=plt.subplots(figsize=(12,4))
ax.bar(x='Attrition', height='DistanceFromHome', data=df, label='DistanceFromHome')
ax.bar(x='Attrition', height='TotalWorkingYears', data=df, label='TotalWorkingYears')
ax.set_xticks(df.Attrition)
plt.show()


# The stack bar graph above is showing total number of attrition rate according to total working years and distance from home where the value of yes is more than no. But on comparing there is only slight difference with no as around 38 count and yes is of 40 count number.

# In[21]:


X = df['DistanceFromHome']
Y = df['EmployeeNumber']
Z = df['EmployeeCount']
plt.bar(X, Y,)
plt.bar(X, Z, bottom=Y)
plt.xlabel("Stack Bar")
plt.ylabel("Stack Bar Graph")
plt.show()


# In[22]:


df['Education'].unique()


# #### Pie chart

# In[23]:


df.groupby(['JobSatisfaction']).sum().plot(kind='pie', y = 'YearsAtCompany', autopct='%1.1f%%')
plt.title('JobSatisfaction')

# x = df["YearsAtCompany"]
# y = df["JobSatisfaction"]
# plt.pie(x,labels=y,autopct='%.2f%%')


# This Pie Chart is describe very high & low coloum in jobsatisfaction & YearsAtCompany 

# #### Scatter Plot

# In[24]:


df.plot.scatter(x='BusinessTravel',y='MonthlyIncome', colormap='viridis',figsize=[5,5])
plt.title('BusinessTravel vs MonthlyIncome')


# This Chart is Showing Total Monthly Income According To BusinessTravel. People Who Travel Rarely ,Frequently or Non-Travler.   

# #### Box Plot

# In[25]:


sns.set_style("darkgrid")
plt.figure(figsize=(4,2))
sns.boxplot(df['Age'], df['Education'])


# This is Box Graph.
# This Graph is Describe Age According To Education.

# #### Histogram Graph

# In[26]:


plt.hist(x=df['Age']);


# This Histogram Graph is Show How Many Age people High In Age Coloum.

# ### seaborn Graph
# * Line plot
# * Countplot
# * Bar chart
# * Pairplot
# * Scatter plot
# * Histogram

# #### Line plot

# In[27]:


x=df['Age']
y=df['TotalWorkingYears']
sns.lineplot(x,y,color='red')


# This is Line Graph. This Graph Show Age Accoriding To Totalworkingyear.

# #### Count plot

# In[28]:


x=df['StockOptionLevel']
y=df['BusinessTravel']
sns.countplot(x,)


# Count Plot Graph Show StockLevel Value In Graph.

# #### Bar chart

# In[29]:


sns.barplot(y=df['TotalWorkingYears'],x=df['Department'], data=df)


# This Graph Showing Wich Type Of Department And How Many Year Of Working In Department.

# #### Pairplot

# In[30]:


df = pd.read_csv("Employee-Attrition.csv")
sns.pairplot(df,hue='Age')


# This is Pair plot Graph.

# #### Scatter plot

# In[49]:


# x=df['Age']
# y=df['TotalWorkingYears']
sns.scatterplot(df['Education'],df['Age'])


# This is scatter plot Graph. This Graph show Education level according to Age.

# In[48]:


df.head()


# This is Scatter Plot Graph And This Graph is Describe 

# #### Histogram

# In[32]:


x=df['MonthlyIncome']
# y=df['']
sns.distplot(x,)


# This is Histogram Graph and this graph show Higest MonthlyIncome.

# In[33]:


df.hist(bins=40 , figsize=(20,20)) #Pandas Hist function
plt.show()


# This Is Hist Funcation. This Funcation is Show All Graph According Coloumn.

# In[50]:


print(df.corr())


# In[ ]:


df.head()


# In[52]:


newdf = df.drop("BusinessTravel", axis='columns')


# In[53]:


newdf.head()


# In[54]:


dataplot = sns.heatmap(df.corr(), cmap="PuBuGn", annot=True)
plt.show()


# This is Heatmap graph. this graph show all Coloum & Rows in csv file
