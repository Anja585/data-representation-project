import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'collateral'
)

cursor = db.cursor()
sql = '''insert into ea_assets (index,
                                isin_code, 
                                issuance_date, 
                                maturity_date, 
                                coupon_rate, 
                                denomination) values (%s%s%s%s%s%s)
                                '''
values = (2222222, 'DE000A289DC1', '13/02/2022', '13/02/2060', '5', 'EUR')

cursor.execute(sql, values)
cursor.commit()
result = cursor.fetchall()
for x in result:
    print(x) 

db.close()
cursor.close()    

