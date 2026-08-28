# Worksheet 6

Link : https://bcourses.berkeley.edu/courses/1557109/files/95177183?module_item_id=17809269
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import scipy.stats as stats

df = pd.read_csv("/content/diabetes_dataset.csv", header=0)

"""# 1. To get an idea of the data, check the head of the dataframe and types of the columns. Print out the unique values in the outcome column, and the max and min values present in Blood Pressure and Insulin."""

df.head()

print(df.columns)

print(df.dtypes)

print(df['Outcome'].unique())

max_bp = df['BloodPressure'].max()
min_bp = df['BloodPressure'].min()
max_insulin = df['Insulin'].max()
min_insulin = df['Insulin'].min()

print("Max Blood Pressure:", max_bp)
print("Min Blood Pressure:", min_bp)
print("Max Insulin:", max_insulin)
print("Min Insulin:", min_insulin)

"""# Question 2 Make a scatterplot of Glucose versus Insulin levels. Next, make a scatterplot of Glucose versus Insulin levels only using rows of the data where neither value is 0."""

x = df['Glucose']
y = df['Insulin']

plot.scatter(x,y)

x = df[ (df['Glucose']!=0) & ((df['Insulin']!=0))]['Glucose']
y = df[ (df['Glucose']!=0) & ((df['Insulin']!=0))]['Insulin']

plot.scatter(x,y)

"""# Question 3 Modify the Pregnancies table to only have 0 or 1 depending on whether the patient has had 0 or more than 0 pregnancies. Then make a pivot table with pregnancies and outcome as the index and columns, and glucose as the value."""

df['Pregnancies'] = np.where( df['Pregnancies']==0,0,1)

pivot_df = df.pivot_table(
      index='Pregnancies',
      columns="Outcome",
      values="Glucose",
      aggfunc="mean"
)

display(pivot_df)

"""# Question 4 Within rows with a nonzero entry for skin thickness: Find the mean of skin thickness, and print out the ’outcome’ percentage of patients with skin thickness above versus below the mean"""

skin_thickness = df["SkinThickness"]
nonzero_skin_thickness = skin_thickness != 0

skin_thickness_mean = skin_thickness[nonzero_skin_thickness].mean()

above_skin_mean = nonzero_skin_thickness & (skin_thickness > skin_thickness_mean)
below_skin_mean = nonzero_skin_thickness & (skin_thickness <= skin_thickness_mean)

above_mean_outcome_percentage = df.loc[above_skin_mean, "Outcome"].mean()
below_mean_outcome_percentage = df.loc[below_skin_mean, "Outcome"].mean()

above_outcome = df.loc[above_skin_mean, "Outcome"]
below_outcome = df.loc[below_skin_mean, "Outcome"]

t_test = stats.ttest_ind(above_outcome, below_outcome, equal_var=False)

print("\nMean nonzero skin thickness:", skin_thickness_mean)
print("Outcome percentage above the mean:", above_mean_outcome_percentage)
print("Outcome percentage below or equal to the mean:", below_mean_outcome_percentage)
print("t-test p-value is:", t_test.pvalue)

"""# Question 5 Let’s make a new column ’BP Risk’, which is 0 if Bloodpressure is below 90, 1 if it is below 100, 2 if it is below 110, and 3 otherwise. Make a box plot of BMI with your new BP Risk column as the index. (and of course I mean make BP risk 1 if BP is below 100 and above 90, and so on)"""

df['BP Risk'] = np.where(df['BloodPressure']<90,0,
                         np.where(df['BloodPressure']<100,1,
                                  np.where(df['BloodPressure']<110,2,3)
                          )
                         )

df.head()

df['BP Risk'].unique()

