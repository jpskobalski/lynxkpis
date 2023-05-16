from DataProcess import DataProcess

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("Usage: python <script_name> <file_path> <connection_string> <query> <table_name>")
        sys.exit(1)

    file_path = sys.argv[1]
    connection_string = sys.argv[2]
    query = sys.argv[3]
    table_name = sys.argv[4]

    data_process = DataProcess(file_path, connection_string, query, table_name)
    data_process.main()