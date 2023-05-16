from sqlalchemy import create_engine

class DataOutput:
    def __init__(self, kpi_data):
        self.kpi_data = kpi_data

    def write_snowsql(self, connection_string, table_name):
        engine = create_engine(connection_string)
        self.kpi_data.to_sql(table_name, engine, if_exists='append', index=False)