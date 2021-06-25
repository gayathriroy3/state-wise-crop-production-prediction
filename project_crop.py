import pandas as pd
crops=pd.read_csv('cropdata.csv') #delimiter='\t')
crops = crops.reset_index()
#print(crops)
#crops=crops.sort_values('Crop',ascending=True)
#print(crops['Crop'][0:5])

#1
#average_crop_production = crops['Production'].mean()
#print(average_crop_production)




#2
print(crops.columns)
y=crops.groupby('Crop')
print(y)
x=y.sum()
yld = x['Production']/x['Area']
x['Yield']=yld
pd.set_option('display.max_columns', None)
print(x)
max_yield = x['Yield'].max()
print(max_yield)
print(x['Yield'].idxmax()) #coconut has max yield




#print(crops.loc[[crops['Crop']=='Apple']])

crops = crops.set_index(['Crop'])#imp
print(crops.loc['Apple'])

#4

wheat=crops.loc['Wheat']
print(wheat)
state_wise_wheat=wheat.groupby('State').sum()
print(state_wise_wheat)
state_wise_max_wheat=state_wise_wheat['Production'].max()
print(state_wise_max_wheat)
print(state_wise_wheat['Production'].idxmax())  #max wheat production in UP


#3
rice=crops.loc['Rice']
print(rice)
state_wise_rice =rice.groupby('State').sum()
print(state_wise_rice)
if (state_wise_rice['Production']['Odisha'])>(state_wise_rice['Production']['West Bengal']):
    diff=state_wise_rice['Production']['Odisha']-state_wise_rice['Production']['West Bengal']
    print('''Production of rice in Odisha is more than that of West Bengal.Odisha produces %i rice.
Whereas in West Bengal ,it is %i.The difference in their production is %i''',state_wise_rice['Production']['Odisha'],state_wise_rice['Production']['West Bengal'],diff)
else:
    diff=state_wise_rice['Production']['West Bengal']-state_wise_rice['Production']['Odisha']
    print('''Production of rice in West Bengal is more than that of Odisha.West Bengal produces '''+str(state_wise_rice['Production']['West Bengal'])+''' rice.
Whereas in Odisha ,it is '''+ str(state_wise_rice['Production']['Odisha'])+''' .The difference in their production is '''+str(diff))


yld1= state_wise_rice['Production']/state_wise_rice['Area']
state_wise_rice['Yield']=yld1
pd.set_option('display.max_columns', None)
#print(state_wise_rice)
if state_wise_rice['Yield']['Odisha']>state_wise_rice['Yield']['West Bengal']:
    print('''Rice Yield in Odisha is '''+str(state_wise_rice['Yield']['Odisha'])+
          ''' ,which is more than yielded in West Bengal, '''+str( state_wise_rice['Yield']['West Bengal']))
else:
    print('''Rice Yield in West Bengal is '''+str(state_wise_rice['Yield']['West Bengal'])+
          ''' ,which is more than yielded in Odisha, '''+str( state_wise_rice['Yield']['Odisha']))


Odisha_all_years =rice.loc[rice['State']=='Odisha']
Odisha_rice_table =pd.DataFrame(Odisha_all_years,columns=['index','State','Year','Area','Production'])
#created table for odisha rice production
print(Odisha_rice_table)

#max production and respective year
max_production=Odisha_rice_table['Production'].max()
print(max_production)
row_odisha =Odisha_rice_table[Odisha_rice_table['Production']==Odisha_rice_table['Production'].max()]  #Odisha_rice_table.loc[Odisha_rice_table['Production'].idxmax()])
print(row_odisha['Year']['Rice'])

#min prod and year
min_production=Odisha_rice_table['Production'].min()
print(min_production)
row_odisha =Odisha_rice_table[Odisha_rice_table['Production']==Odisha_rice_table['Production'].min()]  #Odisha_rice_table.loc[Odisha_rice_table['Production'].idxmax()])
print(row_odisha['Year']['Rice'])

#yield max and min
yld2=Odisha_rice_table['Production']/Odisha_rice_table['Area']
Odisha_rice_table['Yield']=yld2
pd.set_option('display.max_columns', None)
print(Odisha_rice_table)
max_yield=Odisha_rice_table['Yield'].max()
min_yeild=Odisha_rice_table['Yield'].min()
print('max yield of rice in odisha in year ',Odisha_rice_table[Odisha_rice_table['Yield']==Odisha_rice_table['Yield'].max()]['Year']['Rice'])
print('min yield of rice in odisha in year ',Odisha_rice_table[Odisha_rice_table['Yield']==Odisha_rice_table['Yield'].min()]['Year']['Rice'])
    


wb_all_years =rice.loc[rice['State']=='West Bengal']
wb_rice_table =pd.DataFrame(wb_all_years,columns=['index','State','Year','Area','Production'])
#created table for west bengal rice production
print(wb_rice_table)

#max production and respective year
max_production=wb_rice_table['Production'].max()
print(max_production)
row_wb =wb_rice_table[wb_rice_table['Production']==wb_rice_table['Production'].max()]  #Odisha_rice_table.loc[Odisha_rice_table['Production'].idxmax()])
print(row_wb['Year']['Rice'])

#min prod and year
min_production=wb_rice_table['Production'].min()
print(min_production)
row_wb =wb_rice_table[wb_rice_table['Production']==wb_rice_table['Production'].min()]  #Odisha_rice_table.loc[Odisha_rice_table['Production'].idxmax()])
print(row_wb['Year']['Rice'])

#yield max and min
yld3=wb_rice_table['Production']/wb_rice_table['Area']
wb_rice_table['Yield']=yld2
pd.set_option('display.max_columns', None)
print(wb_rice_table)
max_yield=wb_rice_table['Yield'].max()
min_yeild=wb_rice_table['Yield'].min()
print('max yield of rice in odisha in year ',wb_rice_table[wb_rice_table['Yield']==wb_rice_table['Yield'].max()]['Year']['Rice'])
print('min yield of rice in odisha in year ',wb_rice_table[wb_rice_table['Yield']==wb_rice_table['Yield'].min()]['Year']['Rice'])


import matplotlib.pyplot as plt

#df.plot.pie(y='Tasks',figsize=(5, 5),autopct='%1.1f%%', startangle=90)
#plt.show()
year =Odisha_rice_table.groupby(['Year']).sum()
print(year)
ax=year.plot.pie(y='Production',figsize=(5, 5),autopct='%1.1f%%', startangle=90)
ax.set_title("Yearly rice production in Odisha")
plt.legend(title = "Year:")
plt.show()

year1 =wb_rice_table.groupby(['Year']).sum()
print(year1)
bx =year1.plot.pie(y='Production',figsize=(5, 5),autopct='%1.1f%%', startangle=90,rotatelabels=True)
bx.set_title("Yearly rice production in West Bengal")
plt.legend(title = "Year:")
plt.show()

#5


    


