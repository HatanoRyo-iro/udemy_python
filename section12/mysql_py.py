import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv()

mysql_user = os.getenv('mysql_user')
mysql_password = os.getenv('mysql_password')

# conn = mysql.connector.connect(host='127.0.0.1', user=mysql_user, password=mysql_password)

# cursor = conn.cursor()

# cursor.execute(
#     'CREATE DATABASE test_mysql_database'
# )

# cursor.close()
# conn.close()

conn = mysql.connector.connect(host='127.0.0.1', user=mysql_user, password=mysql_password, database='test_mysql_database')
cursor = conn.cursor()
# cursor.execute('CREATE TABLE persons('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(14) NOT NULL,'
#                'PRIMARY KEY(id))')

# cursor.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
conn.commit()
cursor.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()




cursor.close()
conn.close()