import pymysql

connection = pymysql.connect(host="localhost", port=3306, user="Polina", passwd="Pol12345ina", database="files")
cursor = connection.cursor()

num_imp_lines = 0
num_last_lines = 10000000
query = "INSERT INTO files (`date`, `lat_letters`, `ru_letters`, `int_num`, `float_num`) VALUES (%s, %s, %s, %s, %s)"
for i in range(1, 100 + 1):
    with open(f'texts\\text{i}.txt', 'r') as text_file:
        values = [line.split('||') for line in text_file]
        for value in values:
            value.pop()
        tuple_values = [tuple(x) for x in values]
        try:
            cursor.executemany(query, tuple_values)
            connection.commit()
            num_imp_lines += 100000
            num_last_lines -= 100000
            print("Импортировано строк: ", num_imp_lines)
            print("Осталось строк: ", num_last_lines)
        except:
            connection.rollback()
    text_file.close()
connection.close()
