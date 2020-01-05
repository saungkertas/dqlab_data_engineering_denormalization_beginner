import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://guest:relational@relational.fit.cvut.cz/UW_std')
person = pd.read_sql_table('person', engine)
taught_by = pd.read_sql_table('taughtBy', engine)
advised_by = pd.read_sql_table('advisedBy', engine)
course = pd.read_sql_table('course', engine)

person_join_taughtby = person.set_index('p_id').join(taught_by.set_index('p_id'))
person_taughtby_join_advisedby = person_join_taughtby.join(advised_by.set_index('p_id'))
person_taughtby_advisedby_reset_index = person_taughtby_join_advisedby.reset_index()
person_taughtby_advisedby_join_course = person_taughtby_advisedby_reset_index.set_index('course_id').join(course.set_index('course_id'))
full_dataset = person_taughtby_advisedby_join_course.reset_index()                                                                                                  
full_dataset.to_csv('education.csv')