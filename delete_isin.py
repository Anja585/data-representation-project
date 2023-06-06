import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'collateral'
)

cursor = db.cursor()
sql = "delete from ea_assets where isin_code = %s" 
values = ('CCCCC1',)

cursor.execute(sql, values)
db.commit()

db.close()
cursor.close()    

