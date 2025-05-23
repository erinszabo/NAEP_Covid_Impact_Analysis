
from db_connection import connect_to_db

import pandas as pd
import seaborn as sb

conn = connect_to_db()

# pull data into data frames
df_r_t = pd.read_sql("SELECT * FROM reading_trimmed", con=conn)
df_m_t = pd.read_sql("SELECT * FROM math_trimmed", con=conn)

# export to CSV
df_m_t.to_csv("output/m_trimmed.csv", index=False)
df_r_t.to_csv("output/r_trimmed.csv", index=False)




######## END ############
conn.dispose()
"""
^ this will either be the last command in this file or the 
last command in the visuals file if we need to work with the 
actual SQL for visuals. hopefully I can just take out what I need
as some kind of python objects and create visuals with those.
"""
    

#########################

def analysis():
    """"""
    pass

############# helper functions below #################

