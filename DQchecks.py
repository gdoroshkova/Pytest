import pyodbc


def get_db_settings(file_name):
    with open(file_name, "r") as file:
        data = file.read()
        rows = data.splitlines()
        values_list = []
        for row in rows:
            val = row.split("=")
            values_list.append(val[1])
        return values_list


def db_connection(parameters_list):
    server_name = parameters_list[0]
    database_name = parameters_list[1]
    login = parameters_list[2]
    password = parameters_list[3]
    with pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'+f'SERVER={server_name};DATABASE={database_name};UID={login};PWD={password};Encrypt=no', autocommit=True) as connection:
        cursor = connection.cursor()
        return cursor


def check_duplicates(table_name, column_name):
    parameters_list = get_db_settings('db_settings.txt')
    cursor = db_connection(parameters_list)
    cursor.execute(f'SELECT COUNT(*) FROM {table_name} GROUP BY {column_name} HAVING COUNT(*) > 1')
    result = cursor.fetchall()
    cursor.close()
    return result


def check_amount_of_rows(table_name):
    parameters_list = get_db_settings('db_settings.txt')
    cursor = db_connection(parameters_list)
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    result = cursor.fetchall()
    result = result[0][0]
    cursor.close()
    return result


def check_avg_for_column(table_name, column_name):
    parameters_list = get_db_settings('db_settings.txt')
    cursor = db_connection(parameters_list)
    cursor.execute(f'SELECT AVG({column_name}) FROM {table_name}')
    result = cursor.fetchall()
    result = result[0][0]
    cursor.close()
    return result


def check_max_for_column(table_name, column_name):
    parameters_list = get_db_settings('db_settings.txt')
    cursor = db_connection(parameters_list)
    cursor.execute(f'SELECT MAX({column_name}) FROM {table_name}')
    result = cursor.fetchall()
    result = result[0][0]
    cursor.close()
    return result


def check_date_correctness(table_name, date_column):
    parameters_list = get_db_settings('db_settings.txt')
    cursor = db_connection(parameters_list)
    cursor.execute(f'SELECT {date_column} FROM {table_name} WHERE {date_column} IS NULL OR {date_column} > GETDATE()')
    result = cursor.fetchall()
    cursor.close()
    return result


def check_column_for_null_values(table_name, column_name):
    parameters_list = get_db_settings('db_settings.txt')
    cursor = db_connection(parameters_list)
    cursor.execute(f'SELECT {column_name} FROM {table_name} WHERE {column_name} IS NULL')
    result = cursor.fetchall()
    cursor.close()
    return result

