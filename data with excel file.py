# PROBLEM STATEMENT:
# 1. Input a dataset from excel and create a dataframe (dataset of usage of different apps in different cities).
# 2. find the max usage of app in each city.
# 3. group the data for usage of app in different cities using groupby() method.
# 4. Visualize the usage of apps in different cities in all possible plots.



import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df1 = pd.read_excel('excel.xlsx',index_col=[0],header=[0,1],delim_whitespace=True)
print(df1)


#group by function
df3=df1.groupby([('FACEBOOK','CITY1'),('FACEBOOK','CITY2'),('FACEBOOK','CITY3')])
print(df3)

print("***********GROUPING USAGE OF APPS(in hrs)*************(")
for FACEBOOK,app in df3:

    print(app)


#max usage in each city
df2 = df1.max(axis=0)
print("********MAXIMUM USAGE OF APPS IN DIFFERENT CITIES********",df2)

print(df1.columns)      #prints how multi_indexing is working





#graph
x1=["00:00-4:00","4:00-8:00 ","8:00-12:00","12:00-16:00"]
y1=df1[('FACEBOOK','CITY1')]        # plot for facebook
plt.plot(x1,y1,label='city1')

y2=df1[('FACEBOOK','CITY2')]
plt.plot(x1,y2,label='city2')

y3=df1[('FACEBOOK','CITY3')]
plt.plot(x1,y3,label='city3')
plt.xlabel('TIME(in hrs)')
plt.ylabel('APP USAGE(in hrs)')
plt.legend()
plt.title("Facebook")
plt.show()

b1 =df1[('WHATSAPP','CITY1')]    # plot for whatsapp
plt.plot(x1,b1,label='city1')

b2 =df1[('WHATSAPP','CITY2')]
plt.plot(x1,b2,label='city2')

b3 =df1[('WHATSAPP','CITY3')]
plt.plot(x1,b3,label='city3')

plt.xlabel('TIME(in hrs)')
plt.ylabel('APP USAGE(in hrs)')
plt.legend()
plt.title("WHATSAPP")
plt.show()

c1 =df1[('YOUTUBE','CITY1')]   # plot for youtube
plt.plot(x1,c1,label='city1')

c2 =df1[('YOUTUBE','CITY2')]
plt.plot(x1,c2,label='city2')

c3 =df1[('YOUTUBE','CITY3')]
plt.plot(x1,c3,label='city3')

plt.xlabel('TIME(in hrs)')
plt.ylabel('APP USAGE(in hrs)')
plt.legend()
plt.title("YOUTUBE")
plt.show()





#Bar Plot
plt.bar(x1,y1,label='city1',color='r')   #bar plot for facebook
plt.bar(x1,y2,label='city2',color='g')
plt.bar(x1,y3,label='city3',color='b')
plt.legend()
plt.title("FACEBOOK")
plt.show()

plt.bar(x1,b1,label='city1',color='r')   #bar plot for whatsapp
plt.bar(x1,b2,label='city2',color='g')
plt.bar(x1,b3,label='city3',color='b')
plt.legend()
plt.title("WHATSAPP")
plt.show()

plt.bar(x1,c1,label='city1',color='r')    #bar plot for youtube
plt.bar(x1,c2,label='city2',color='g')
plt.bar(x1,c3,label='city3',color='b')
plt.legend()
plt.title("YOUTUBE")
plt.show()

#Scatter plot

plt.scatter(x1,y1,label='city1',color="green",marker="*")   #Scatter plot for facebook
plt.scatter(x1,y2,label="city2",color="blue",marker="*")
plt.scatter(x1,y3,label='city3',color='red',marker='*')
plt.legend()
plt.xlabel("Time(in hrs)")
plt.ylabel("APP USAGE(in hrs)")
plt.title("FACEBOOK")
plt.show()

plt.scatter(x1,b1,label='city1',color="green",marker="*")   #Scatter plot for whatsapp
plt.scatter(x1,b2,label="city2",color="blue",marker="*")
plt.scatter(x1,b3,label='city3',color='red',marker='*')
plt.legend()
plt.xlabel("Time(in hrs)")
plt.ylabel("APP USAGE(in hrs)")
plt.title("WHATSAPP")
plt.show()


plt.scatter(x1,c1,label='city1',color="green",marker="*")   #Scatter plot for youtube
plt.scatter(x1,c2,label="city2",color="blue",marker="*")
plt.scatter(x1,c3,label='city3',color='red',marker='*')
plt.legend()
plt.xlabel("Time(in hrs)")
plt.ylabel("APP USAGE(in hrs)")
plt.title("YOUTUBE")
plt.show()






















