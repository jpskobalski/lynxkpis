import pandas as pd
from sqlalchemy import create_engine

# Define the class for data input
class DataInput:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_excel(self):
        self.data = pd.read_excel(self.file_path)
        return self.data

    def read_snowsql(self, connection_string, query):
        engine = create_engine(connection_string)
        self.data = pd.read_sql_query(query, engine)
        return self.data