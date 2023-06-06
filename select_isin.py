import mysql.connector
import pandas as pd


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'collateral'
)

cursor = db.cursor()
sql = "select * from ea_assets where isin_code = %s"
value = ('DE000A289DC9',)

cursor.execute(sql, value)
result = cursor.fetchall()
for x in result:
    print(x) 

db.close()
cursor.close()    

