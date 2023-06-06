import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'collateral'
)

cursor = db.cursor()
sql = '''update ea_assets set   isin_code = %s, 
                                issuance_date = %s, 
                                maturity_date = %s, 
                                coupon_rate = %s, 
                                denomination = %s;
                                '''
values = ('CCCCC1', '13/02/2022', '13/02/2060', 5, 'USD')

cursor.execute(sql, values)
db.commit()

db.close()
cursor.close()    

