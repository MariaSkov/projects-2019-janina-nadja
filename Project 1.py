#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Project1'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd 
import pandas_datareader
from pandas_datareader import wb
import matplotlib.pyplot as plt
import os


#%%
os.getcwd()
# Create new folders:
#os.makedirs('C:\\delicious\\walnut\\waffles')

# #change directory
os.chdir("C:/Users/Janina/Documents/Master/3rd semester/intro to programming/Project1")


#%%
import requests
url = "http://www.sais-cari.org/s/FDIData_04Mar2019.xlsx"
r = requests.get(url)

# with open('test.xls', 'wb') as output:
#     output.write(resp.content)
# print("Done!")
with open('China_Africa.xlsx', "wb") as f:
    f.write(r.content)
# output = open('test.xls', 'wb')
# output.write(r.content)
# output.close()
   


#%%
ChAfr = pd.read_excel('China_Africa.xlsx', skiprows=1)


#%%
ChAfr.head(20)


#%%
#Drop all rows with missing values only
#ChAfr=ChAfr.drop([0,1,2,3,4,5,6,7,8,9,10,11,12], axis=0)
ChAfr = ChAfr[ChAfr['Total, US$ mn']>0]
ChAfr=ChAfr.dropna(axis=1)
ChAfr.head(15)


#%%
#Same for "tail" of data set
ChAfr=ChAfr.drop([28, 29, 30, 31, 32, 33, 34], axis=0)


#%%
ChAfr.head()


#%%
ChAfr=ChAfr.dropna(axis=0)


#%%
#Drop variables with only missing observations
drop = ['Regional', 'Western Sahara', 'Unnamed: 58', 'Swaziland']

ChAfr.drop(drop, axis=1, inplace=True)


#%%
ChAfr.tail(35)


#%%
ChAfr=ChAfr.rename(columns={'US$ mn, unadjusted':'Year'})


#%%
ChAfr.head(20)


