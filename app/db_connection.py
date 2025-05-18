from sqlalchemy import create_engine

def connect_to_db():
    return create_engine("mysql+pymysql://root:root@mysql-db/surveyDB")
