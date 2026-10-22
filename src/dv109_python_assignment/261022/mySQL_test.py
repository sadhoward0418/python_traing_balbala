import mysql.connector

connection = mysql.connector.connect(
    host="10.167.215.63",
    port=3306,
    user="python_course",
    password="1234",
    database="python_course",
)
cursor = connection.cursor(dictionary=True)
cursor.execute(
    "SELECT COUNT(*) AS total FROM learners"
)

row = cursor.fetchone()

if row is None:
    print("沒有查到資料")
else:
    print(row["total"])


print("MySQL 連線成功")
connection.close()

