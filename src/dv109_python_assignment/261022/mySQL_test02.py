import mysql.connector

connection = mysql.connector.connect(
    host="10.167.215.63",
    port=3306,
    user="python_course",
    password="1234",
    database="python_course",
)
print("MySQL 連線成功")
cursor = connection.cursor(dictionary=True)
cursor.execute(
    """
    SELECT id, name, weekly_hours, goal
    FROM learners
    ORDER BY id
    """
)

rows = cursor.fetchall()

for row in rows:
    print(row["name"])

connection.close()