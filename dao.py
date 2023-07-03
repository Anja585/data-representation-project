import mysql.connector

class isinDAO:
    host = "",
    user = "",
    password = "",
    database = ""
    connection = ""
    cursor = ""

    def __init__(self):
        # these should be read from a config file 
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'collateral'
    
    # connection
    def get_cursor(self):
        self.connection = mysql.connector.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        database = self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    # closes the connection
    def close_all(self):
        self.connection.close()
        self.cursor.close()

    # creates one record
    def create(self, values):
        cursor = self.get_cursor()
        sql = '''insert into ea_assets (isin_code, 
                                issuance_date, 
                                maturity_date, 
                                coupon_rate, 
                                denomination) values (%s,%s,%s,%s,%s);
                                '''
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()

    # retrieves all isins
    def get_all(self):
        cursor = self.get_cursor()
        sql = 'select * from ea_assets limit 10'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(type(result))
        self.close_all()
        return result
    
    # find isin by isin code
    def find_isin(self, value):
        cursor = self.get_cursor()
        sql = "select * from ea_assets where isin_code = %s"
        value = (value,)
        cursor.execute(sql, value)
        result = cursor.fetchall()
        self.close_all()
        return result
    
    # updates isin
    def update(self, values):
        cursor = self.get_cursor()
        sql = '''update ea_assets set isin_code = %s, 
                                      issuance_date = %s, 
                                      maturity_date = %s, 
                                      coupon_rate = %s, 
                                      denomination = %s;
                                      '''
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()

    # deletes record    
    def delete(self, value):
        cursor = self.get_cursor()
        sql = "delete from ea_assets where isin_code = %s"
        value = (value,)
        cursor.execute(sql, value)
        self.connection.commit()
        self.close_all()

isinDAO = isinDAO()






    