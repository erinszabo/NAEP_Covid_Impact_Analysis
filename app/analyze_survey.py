
from db_connection import connect_to_db

import pandas as pd
import seaborn as sb

conn = connect_to_db()
# pull data into data frames
df_m = pd.read_sql("SELECT * FROM math_hc", con=conn)
df_r = pd.read_sql("SELECT * FROM reading_hc", con=conn)

df_m.to_csv("output/m_hc_export.csv", index=False)
df_r.to_csv("output/r_hc_export.csv", index=False)


##########################
# just looking ay stuff here
print("------------ndf_m: -------------")
print(df_m)
print("----------------------------------")
print("------------ndf_r: -------------")
print(df_r)
print("----------------------------------")

##########################


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

