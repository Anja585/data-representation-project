import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'collateral'
)

cursor = db.cursor()
sql = '''create table ea_assets(
        isin_code varchar(20), 
        issuance_date varchar(20), 
        maturity_date varchar(20), 
        coupon_rate int, 
        denomination varchar(100), 
        primary key(isin_code));'''

cursor.execute(sql)

db.commit()
db.close()
cursor.close()