import pymysql

QUERY_SUM = "SELECT SUM(int_num) FROM files"
QUERY_MED = """SELECT AVG(dd.float_num) as median_val
FROM (
SELECT d.float_num, @rownum:=@rownum+1 as `row_number`, @total_rows:=@rownum
  FROM files d, (SELECT @rownum:=0) r
  WHERE d.float_num is NOT NULL
  ORDER BY d.float_num
) as dd
WHERE dd.row_number IN ( FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2) );"""


def count_sum_med(query):
    connection = pymysql.connect(host="localhost", port=3306, user="Polina", passwd="Pol12345ina", database="files")
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()[0][0]
        connection.close()
        return result
    except:
        connection.rollback()


print("Сумма целых: ", count_sum_med(QUERY_SUM), '\n', "Медиана дробных: ", count_sum_med(QUERY_MED))
