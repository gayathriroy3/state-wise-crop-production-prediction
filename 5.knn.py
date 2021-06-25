#import numpy as np
#from sklearn.linear_model import LinearRegression
#model = LinearRegression()

import pandas as pd
crops=pd.read_csv('cropdata.csv') #delimiter='\t')
#crops = crops.reset_index()
crops = crops.set_index(['Crop'])
rice=crops.loc['Rice']
print(rice)
ap_all_years =rice.loc[rice['State']=='Andhra Pradesh']
print(ap_all_years)

from sklearn.model_selection import train_test_split
train,test = train_test_split(ap_all_years,test_size=0.3,random_state=0)

x_train = train.drop('Production' ,axis=1)
y_train=train['Production']

x_test = test.drop('Production' ,axis=1)
y_test=test['Production']
x_train=x_train.drop('State',axis=1)
x_test=x_test.drop('State',axis=1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

#scaling
'''from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
print(x_train.columns)
x_train_scaled=scaler.fit_transform(x_train.values)
x_train=pd.DataFrame(x_train_scaled)
print(x_train)'''

from sklearn.neighbors import KNeighborsRegressor as KNN
from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt
#def Elbow(K):
 #   test_error=[]
  #  for i in K:
        
#        clf=KNN(n_neighbors=i)
#        clf.fit(x_train,y_train)
#        test_predict=clf.predict(x_test)
#        tmp=mse(test_predict,y_test)
#        test_error.append(tmp)
#    print(test_error)
#k=range(1,6)
#test=Elbow(k)
#plt.plot(k,test)
#plt.xlabel('kNeighbors')
#plt.ylabel('Test Error')
#plt.title('Elbow Curve')
#plt.show()
reg=KNN(n_neighbors=1)
reg.fit(x_train,y_train)
test_predict=reg.predict(x_test)
tmp=mse(test_predict,y_test)
print(tmp)
from sklearn.metrics import mean_absolute_error as mae
tmp1=mae(test_predict,y_test)
print(tmp1)
mean_value=ap_all_years['Area'].mean()
print(mean_value)
new_x=[[2014,mean_value]]
x=pd.DataFrame(new_x,columns=['Year','Area'])
print(reg.predict(x))







    
