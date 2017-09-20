#Program Name: Data Preprocessing
#Student Name: Muni Bhupathi Reddy Dandu
#Mwsu Id     : M20228454

#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset=pd.read_csv('mortgage_rates.csv')
#simple linear regression Y=MX+C
#Y-Dependent,X-Independent

#independent dataset
X=dataset.iloc[:,1:-1].values
#dependent dataset
y=dataset.iloc[:,2].values
for i in range(0,len(y)):
    #removing $ from the median home price values
    y[i]=y[i].replace("$","")
    #removing , from the median home price values
    y[i]=y[i].replace(",","")

#converting string type to int
y=y.astype(int)

#Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=1/3,random_state=0)

#Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

#Predicting the Test set results
y_pred=regressor.predict(X_test)

#Visualising the Training set results
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Median Home Price vs Interest Rate (Training set)')
plt.xlabel('Interest Rate')
plt.ylabel('Meidan Hmoe Price')
plt.show()

#Visualising the Test set results
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Median Home Price vs Interest Rate (Test set)')
plt.xlabel('Interest Rate')
plt.ylabel('Meidan Hmoe Price')
plt.show()
