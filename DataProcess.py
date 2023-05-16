from dataInput.DataInputService import DataInput
from dataOutput.DataOutputService import DataOutput
from kpiCalculation.KpiCalculation import KPICalculation

class DataProcess:
    def __init__(self, file_path, connection_string, query, table_name):
        self.file_path = file_path
        self.connection_string = connection_string
        self.query = query
        self.table_name = table_name

    def main(self):
        data_input = DataInput(self.file_path)
        data = data_input.read_excel()  # or data_input.read_snowsql(self.connection_string, self.query)

        kpi_calculation = KPICalculation(data)
        kpi1 = kpi_calculation.calculate_kpi1()
        kpi2 = kpi_calculation.calculate_kpi2()

        data_output = DataOutput(kpi1)  # or DataOutput(kpi2)
        data_output.write_snowsql(self.connection_string, self.table_name)