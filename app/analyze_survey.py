
from db_connection import connect_to_db

import pandas as pd
import seaborn as sb

conn = connect_to_db()
# pull data into data frames
df_m = pd.read_sql("SELECT * FROM math_hc", con=conn)
df_r = pd.read_sql("SELECT * FROM reading_hc", con=conn)

# possibly get rid of these lower two, if I get rid of sql 4 file
#  OR use only these, let them be df_m and df_r
##df_m_nomissing = pd.read_sql("SELECT * FROM math_no_missing", con=conn)
##df_r_nomissing = pd.read_sql("SELECT * FROM reading_no_missing", con=conn)

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

