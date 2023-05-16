import pandas as pd
from snowflake.sqlalchemy import URL
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


# Define the class for KPI calculations
class KPICalculation:
    def __init__(self, data):
        self.data = data

    def calculate_kpi1(self):
        # Define your KPI calculation logic here
        pass

    def calculate_kpi2(self):
        # Define your KPI calculation logic here
        pass


# Define the class for data output
class DataOutput:
    def __init__(self, kpi_data):
        self.kpi_data = kpi_data

    def write_snowsql(self, connection_string, table_name):
        engine = create_engine(connection_string)
        self.kpi_data.to_sql(table_name, engine, if_exists='append', index=False)


# Main program
if __name__ == "__main__":
    # Define your file path or connection string and query
    file_path = "path_to_your_file"
    connection_string = "your_connection_string"
    query = "your_query"
    table_name = "your_table_name"

    data_input = DataInput(file_path)
    data = data_input.read_excel()  # or data_input.read_snowsql(connection_string, query)

    kpi_calculation = KPICalculation(data)
    kpi1 = kpi_calculation.calculate_kpi1()
    kpi2 = kpi_calculation.calculate_kpi2()

    data_output = DataOutput(kpi1)  # or DataOutput(kpi2)
    data_output.write_snowsql(connection_string, table_name)