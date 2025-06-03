# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:02:52 2024

@author: ritidahal
"""
import pandas as pd   ###importing pandas packages
import matplotlib.pyplot as plt  ######used to plot and visulaization of data
import seaborn as sns  ####used for creating statistical graph like box plot and scatter plot with regression line
import scipy.stats as st ####used for regression line 

###Reading a data 
obesitydata = pd.read_csv("C:/Users/rewaz/OneDrive/Desktop/BA/Obesity Data Set.csv")
###Displays the first five rows of a dataset
obesitydata.head()

#####Shows total number of columns, rows, data type
obesitydata.info()

#####Shows if there is any missing values in a data set. No missing values in this data set
obesitydata.count()

######Shows the total number of observation
len(obesitydata)

#####Shows the number of rows and columns
obesitydata.shape

#####Find the count, mean, standard deviation, min and max of numeric variables from the data set
descriptivestat = obesitydata.describe()


####Checking the outliers for the numeric variables 
#####Age
A_25 = obesitydata.Age.quantile(0.25)
A_75 = obesitydata.Age.quantile(0.75)
IQR = A_75-A_25
LowerFence = A_25 - 1.5*IQR
UpperFence = A_75 + 1.5*IQR
obesitydata.Age.max()
obesitydata.Age.min()
#####Plotting the box plot
obesitydata[['Age']].plot(kind='box')

#####Capping the outliers
new_obesitydata = obesitydata.copy()
new_obesitydata.loc[new_obesitydata['Age'] > UpperFence, 'Age'] = UpperFence
new_obesitydata.loc[new_obesitydata['Weight'] < LowerFence, 'Weight'] = LowerFence
len(new_obesitydata)

####Plotting the new box plot after removing outliers
new_obesitydata[['Age']].plot(kind='box')                     


####Weight
W_25 = obesitydata.Weight.quantile(0.25)
W_75 = obesitydata.Weight.quantile(0.75)
IQR = W_75-W_25
LowerFence = W_25 - 1.5*IQR
UpperFence = W_75 + 1.5*IQR
obesitydata.Weight.max()
obesitydata.Weight.min()
#####Plotting the box plot
obesitydata[['Weight']].plot(kind='box')

#####Capping the outliers
new_obesitydata = obesitydata.copy()
new_obesitydata.loc[new_obesitydata['Weight'] > UpperFence, 'Weight'] = UpperFence
new_obesitydata.loc[new_obesitydata['Weight'] < LowerFence, 'Weight'] = LowerFence
len(new_obesitydata)

####Plotting the new box plot after removing outliers
new_obesitydata[['Weight']].plot(kind='box')   

#####Height
H_25 = obesitydata.Height.quantile(0.25)
H_75 = obesitydata.Height.quantile(0.75)
IQR = H_75-H_25
LowerFence = H_25 - 1.5*IQR
UpperFence = H_75 + 1.5*IQR
obesitydata.Height.max()
obesitydata.Height.min()
#####Plotting the box plot
obesitydata[['Height']].plot(kind='box')

#####Capping the outliers
new_obesitydata = obesitydata.copy()
new_obesitydata.loc[new_obesitydata['Height'] > UpperFence, 'Height'] = UpperFence
new_obesitydata.loc[new_obesitydata['Height'] < LowerFence, 'Height'] = LowerFence
len(new_obesitydata)
####Plotting the new box plot after removing outliers
new_obesitydata[['Height']].plot(kind='box')   


####CH2O
CH2O_25 = obesitydata.CH2O.quantile(0.25)
CH2O_75 = obesitydata.NCP.quantile(0.75)
IQR = CH2O_75-CH2O_25
LowerFence = CH2O_25 - 1.5*IQR
UpperFence = CH2O_75 + 1.5*IQR
obesitydata.CH2O.max()
obesitydata.CH2O.min()
#####Plotting the box plot
obesitydata[['CH2O']].plot(kind='box')

#####FAF
FAF_25 = obesitydata.FAF.quantile(0.25)
FAF_75 = obesitydata.FAF.quantile(0.75)
IQR = FAF_75-FAF_25
LowerFence = FAF_25 - 1.5*IQR
UpperFence = FAF_75 + 1.5*IQR
obesitydata.FAF.max()
obesitydata.FAF.min()
#####Plotting the box plot
obesitydata[['FAF']].plot(kind='box')

#####TUE
TUE_25 = obesitydata.TUE.quantile(0.25)
TUE_75 = obesitydata.TUE.quantile(0.75)
IQR = TUE_75-TUE_25
LowerFence = TUE_25 - 1.5*IQR
UpperFence = TUE_75 + 1.5*IQR
obesitydata.TUE.max()
obesitydata.TUE.min()
#####Plotting the box plot
obesitydata[['TUE']].plot(kind='box')

#####NObeyesdad
OL_25 = obesitydata.NObeyesdad.quantile(0.25)
OL_75 = obesitydata.NObeyesdad.quantile(0.75)
IQR = OL_75-OL_25
LowerFence = OL_25 - 1.5*IQR
UpperFence = OL_75 + 1.5*IQR
obesitydata.NObeyesdad.max()
obesitydata.NObeyesdad.min()
#####Plotting the box plot
obesitydata[['NObeyesdad']].plot(kind='box')


####Using lambda functionality, changing Age into an integer
obesitydata['Age_clean'] = obesitydata['Age'].apply(lambda x: None if x < 18 else x)
obesitydata['Age_clean'] = obesitydata['Age_clean'].round()
obesitydata[['Age', 'Age_clean']]

######Showing Distribution Plot
sns.distplot(new_obesitydata.Age, bins=15)
sns.distplot(new_obesitydata.Weight, bins=15)
sns.distplot(new_obesitydata.Height, bins=15)
sns.distplot(obesitydata.NObeyesdad, bins=15)
plt.xlabel('Obesity Level')
plt.show()
sns.distplot(new_obesitydata.CH2O, bins=15)
plt.xlabel('Water Intake')
plt.show()

####Showing the relationships using count plots
sns.countplot(data=obesitydata, x='family_history_with_overweight')
sns.countplot(data=obesitydata, x='FAVC')
sns.countplot(data=obesitydata, x='SMOKE')
sns.countplot(data=obesitydata, x='NObeyesdad')
sns.countplot(data = obesitydata, x='CALC')
plt.xlabel('Caloric Food')
plt.show()





#######Box Plot to compare Calorie Count and Weight
sns.boxplot(data=new_obesitydata, x='FAVC', y='Weight') ###compares two box plot
plt.title('Calorie Count and Weight') ###displays title
plt.xlabel('Calorie Count') ###displays label in x-axis
plt.ylabel('Weight') ###displays label in y-axis
# Shows the box plot
plt.show()

######Relationship Between Obesity Level and Weight
sns.boxplot(data=new_obesitydata, x='NObeyesdad', y='Weight')
#Adding Titles to show the comparison between Obesity Level and Weight
plt.title('Obesity Level and Weight')
plt.xlabel('Obesity Level')
plt.ylabel('Weight')
# Shows the box plot
plt.show()

##########Box Plot for Obesity Level and Weight
new_obesitydata[['NObeyesdad','Weight']].plot(kind='box')
plt.title('Obesity Level and Weight')
plt.xlabel('Obesity Level')
plt.ylabel('Weight')
# Shows the box plot
plt.show()

####Box Plot for Family History and Weight
sns.boxplot(data=obesitydata, x='family_history_with_overweight', y='Weight')
#Adding Titles to show the comparison between Weight and Family History
plt.title('Weight Vs. Family History with Overweight')
plt.xlabel('Family History with Overweight')
plt.ylabel('Weight')
# Shows the box plot
plt.show()

obesitydata[['family_history_with_overweight','Weight']].plot(kind='box')
plt.title('Family History and Weight')
plt.xlabel('Family History with Overweight')
plt.ylabel('Weight')
# Shows the box plot
plt.show()


### Exploring the relationship between Physical Activity and Use of Technological Devices
### XY Scatterplot
obesitydata.plot.scatter('NObeyesdad', 'Weight')
### Using Seaborn Package
import seaborn as sns
sns.scatterplot(x = obesitydata.NObeyesdad, y = obesitydata.Weight)
### Correlation Coefficient
### Using Pandas
df_vals = obesitydata[['NObeyesdad', 'Weight']]
df_vals.corr()
### Using SciPy Stats
corr = st.pearsonr(obesitydata.NObeyesdad, obesitydata.Weight)
print("Pearson's Correlation Coefficient = ", corr[0])
print("The p-value for testing rho = 0 is: ", corr[1])

### Simple Linear Regression
lm1 = st.linregress(obesitydata.NObeyesdad, obesitydata.Weight)

intercept = lm1[1]
slope = lm1[0]

### Add Regression Line onto Scatterplot

plt.scatter(obesitydata.FAF, obesitydata.TUE)
plt.plot(obesitydata.FAF, intercept + slope*obesitydata.FAF, color = 'red')
plt.title("Physical Activity and Use of Technological Devices")
plt.show()

###########Exploring the relationship between Age and FAF (Physical Activity of an Individual)
obesitydata.plot.scatter('Age', 'FAF')
### Using Seaborn Package
import seaborn as sns
sns.scatterplot(x = obesitydata.Age, y = obesitydata.FAF)
### Correlation Coefficient
### Using Pandas
df_vals = obesitydata[['Age', 'FAF']]
df_vals.corr()
### Using SciPy Stats
corr = st.pearsonr(obesitydata.Age, obesitydata.FAF)
print("Pearson's Correlation Coefficient = ", corr[0])
print("The p-value for testing rho = 0 is: ", corr[1])

### Simple Linear Regression
lm1 = st.linregress(obesitydata.Age, obesitydata.FAF)

intercept = lm1[1]
slope = lm1[0]

### Add Regression Line onto Scatterplot
import matplotlib.pyplot as plt
plt.scatter(obesitydata.Age, obesitydata.FAF)
plt.plot(obesitydata.Age, intercept + slope*obesitydata.Age, color = 'red')
plt.title("Age vs Physical Activity")
plt.show()



######Scatterplot between Height and Weight
sns.scatterplot(x = obesitydata.Height, y = obesitydata.Weight)
plt.title('Height vs Weight')
plt.show()

obesitylevel = obesitydata.pivot_table(index='Gender', columns='FAF', aggfunc='sum')
obesitydata.plot()

# Bar chart showing relationship between Gender and Physical Activity 
sns.barplot(x='Gender', y='FAF', data= new_obesitydata)
plt.title('Physical Activity and Gender')
plt.xlabel('Gender')
plt.ylabel('Physical Activity')
plt.show() 


#####Bar chart showing relationship between Obesity Level and Age
sns.barplot(x='NObeyesdad', y='Age', data= obesitydata)
plt.title('Physical Activity and Gender')
plt.xlabel('Gender')
plt.ylabel('Physical Activity')
plt.show() 



####plotting histogram for NCP
obesitydata['NCP'].plot(kind='hist', bins=30)

#####Bar chart
pivot = obesitydata.pivot_table(values='Weight', index='Age', columns='NObeyesdad',aggfunc='count')
pivot.plot(kind='bar')

###Bar chart showing the relationship between FCVC and NCP
obesitydata[['FCVC', 'NCP']].plot(kind='bar')

######Comparing Male and Females Weight
g = sns.FacetGrid(obesitydata, col='Gender', height=5)
g = g.map(sns.histplot, 'Weight') ####combines two histogram to show the comparison
