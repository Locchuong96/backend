import pandas as pd 
import numpy as np 
from sqlalchemy import create_engine

df = pd.read_excel('result.xlsx')
df = df.drop(['Unnamed: 0'],axis =1)

#create a data and the connection
# set echo = True to see all output that comes from our database
# engine  = create_engine('sqlite:///data.db?charset=utf8',echo = True)
engine  = create_engine('sqlite:///data.db?charset=utf8&use_unicode=0',echo = True)
sqlite_connection = engine.connect()

# save data table name, if_exists 'fail','replace','append'
df.to_sql("Realestate",sqlite_connection,if_exists =  'fail',index_label = 'id')

sqlite_connection.close()

print("database generated!")


