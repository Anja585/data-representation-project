import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'collateral'
)

cursor = db.cursor()
sql = '''insert into ea_assets (isin_code, 
                                issuance_date, 
                                maturity_date, 
                                coupon_rate, 
                                denomination) values (%s,%s,%s,%s,%s);
                                '''
values = ('CCCCC1', '13/02/2022', '13/02/2060', 5, 'EUR')

cursor.execute(sql, values)
db.commit()

db.close()
cursor.close()    

