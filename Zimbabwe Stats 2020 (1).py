#!/usr/bin/env python
# coding: utf-8

# In[112]:


#importing the first sql libary for py withoout math functionality; but credentials adoptions 
import ibm_db


# In[113]:


#The database credentials to teh db2 warehouse to access the tables.
#These credentials are only for an instance in the cloud account, that allows one instance per session

dsn_driver = "IBM DB2 ODBC DRIVER"
dsn_database = "BLUDB"

dsn_hostname = "dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net"
dsn_port = "50000"
dsn_protocol = "TCPIP"   

dsn_uid = "bfp69501"
dsn_pwd= "xr2wcxn5tzkdt@lp"


# In[114]:


dsn = (
    "DRIVER = {0};"
    "DATABASE = {1};"
    "HOSTNAME = {2};"
    "PORT= {3};"
    "PROTOCOL= {4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)


# In[115]:


try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )


# In[151]:


#NB this API may take a while before it connects an instance to the IBM DB2 free services
#Please run the code multiple times, if you are prompted for with a warning for expired credentials do not hesitate to contact me 


# In[117]:


#Retrieve Metadata for the Database Server
server = ibm_db.server_info(conn)

print ("DBMS_NAME: ", server.DBMS_NAME)
print ("DBMS_VER:  ", server.DBMS_VER)
print ("DB_NAME:   ", server.DB_NAME)

#Retrieve Metadata for the Database Client / Driver
client = ibm_db.client_info(conn)
print(client)


# In[118]:


#import libraries for math and plots; establish a different ibm API to retrieve and show data contained
import pandas
import numpy
import scipy 
from scipy import stats
import ibm_db_dbi
import matplotlib 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[119]:


#The code below will now show the data that we are working with; that is stored and structured in tables in DB2

#connection for pandas
pconn = ibm_db_dbi.Connection(conn)
instance1= "select * from CPI" 
instance2 = "select * from ECOINDI"
instance3 = "select * from CRISIS" 
show1 = pandas.read_sql(instance1, pconn)   #this data is now in pandas dataframe 
show2 = pandas.read_sql(instance2, pconn)
show3 = pandas.read_sql(instance3, pconn)


# In[ ]:





# In[120]:



print("Consumer Price Index") 
CPI = show1.drop(["Consumer_Price_Index___February_2019_100_", "Column_2", "Column_3", "Column_4", "Column_5", "Column_6","Column_7", "Column_8", "Column_9", "Column_10", "Column_11", "Column_12", "Column_13"], axis = 1)
CPI.columns=['CPI_mt', 'Prd_All_Items' , 'Inflation_Rate_Percent_Monthly', 'Inflation_Rate_Percent_Annual']
CPi= CPI.replace('None', '').astype(str)
CPi.head(5)


# In[157]:



print("Macro-economic Indicators")
show2= show2.replace('None', '').astype(str)
show2.columns=['Indicator', '2009' , '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
show2.head(8)


# In[153]:


#Do not drop all countries before comparison we might nedd the data 
#juy = range(969)
#show4= show3.drop(index=juy, axis= 0)

print("Global economic crisis")
show4 = show3.drop(["inflation_crises", "case", "banking_crisis", "currency_crises", "domestic_debt_in_default", "sovereign_external_debt_default", "gdp_weighted_default","independence"], axis = 1)
show4= show4.replace('None', '').astype(str)
show4.head(5)
#refined global economic crisis data


# In[144]:


CPi.dtypes


# In[124]:



 show2.dtypes


# In[125]:



show4.dtypes


# In[126]:


#modification of the cpi and defination of attributes

df_CPi = cpi.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

df_CPi = df_cpi.replace("None", "").astype(str)

df_CPi['CPI_mt'] = pandas.to_numeric(df_cpi['CPI_mt'], errors='coerce')

df_CPi['Prd_All_Items'] = pandas.to_numeric(df_cpi['Prd_All_Items'], errors='coerce')

df_CPi['Inflation_Rate_Percent_Monthly'] = pandas.to_numeric(df_cpi['Inflation_Rate_Percent_Monthly'], errors='coerce')

df_CPi['Inflation_Rate_Percent_Annual'] = pandas.to_numeric(df_cpi['Inflation_Rate_Percent_Annual'], errors= 'coerce')

df_CPi.dtypes


# In[149]:


# modification of crisis modification of attributes 
#let all pythin programmers take time to acknowledge the programmer who invented the pandas module i been stressing the whole day!!!!

show4['exch_usd'] = pandas.to_numeric(show4['exch_usd'], errors='coerce')

show4['inflation_annual_cpi'] = pandas.to_numeric(show4['inflation_annual_cpi'], errors='coerce')

show4['year'] = pandas.to_datetime(show4['year'], errors='coerce')


show4.dtypes


# In[133]:


#essentials establieshed on Consumer Price Index Data and global crisi data  Now its time for some real Maths :)

#Import magic sql environment to view tables for plots

get_ipython().system('pip install ipython-sql')


# In[134]:


get_ipython().run_line_magic('load_ext', 'sql')

get_ipython().run_line_magic('sql', 'ibm_db_sa://bfp69501:xr2wcxn5tzkdt%40lp@dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net:50000/BLUDB')


try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to Tinashe's Db2: ", dsn_database, "As user: ", dsn_uid, "on Host: ", dsn_hostname)

except:
    print ("Unable to connect, Logon Instance can not exceed 5! Try Again a bit later/ Read Error and contact Tinashe for Help :)", ibm_db.conn_errormsg() )
    


# In[143]:



gk = get_ipython().run_line_magic('sql', ' SELECT * FROM ECOINDI')
gk
#this SQL code will hold the dataframe in a scaled tabular view to show other indicators that were in the dataset grouped per industrial sector


# In[158]:


#LIST OF USEFUL INDICATORS FOR ANALYSIS 
Indicators=['GDP per capita', 'Export growth (%)', 'Import growth (%)', 'Trade Balance (US$M)', 'POPULATION (millions)']

ecoIndi= pandas.DataFrame(show2, columns = ['Indicator', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'], index=[9, 27, 28, 87])
ecoIndi

#Nice:) 


# In[159]:


#remember now we are working with 
#ecoIndi show4 as crisis CPi as CPi

ecoIndi.describe()


# In[160]:


CPi.describe()  #not useful


# In[161]:


#to be honest Zimbabwe needs more data assets this is useless 
show4.describe() #not useful


# In[ ]:



#income_vs_hardship = %sql SELECT FROM ECOINDI;


#plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())



#Pending developments on this Notebook through GitHub
#WebScrapping In Progress for improvements on Dataset used in this project
#Used data was Free from Kuggle/ RBZ (already Refined)/ 


