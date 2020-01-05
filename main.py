import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://guest:relational@relational.fit.cvut.cz/UW_std')
data = pd.read_sql_table('person', engine)
print(data)