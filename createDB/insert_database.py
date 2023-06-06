from sqlalchemy import create_engine
import pandas as pd

df = pd.read_excel('ea_csv_230523.xlsx')
df = df[['isin_code', 
         'issuance_date', 
         'maturity_date', 
         'coupon_rate', 
         'denomination']] 

engine = create_engine('mysql+pymysql://root:''@localhost/collateral?charset=utf8mb4')

df.to_sql(name='ea_assets', con=engine, if_exists='replace', index=False)

