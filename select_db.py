import mysql.connector
from mysql.connector import connection

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='88881111',
    database='ex10db'
)

mycursor = mydb.cursor()
mycursor.execute('SELECT capital FROM country WHERE name LIKE "E%"')
result = mycursor.fetchall()
for row in result:
    with open('result_select_1.txt', 'w') as file:
        file.write(str(row)+ '\n')

# mycursor.execute('SELECT capital FROM country WHERE name LIKE "I%"')
# result1 = mycursor.fetchall()
# for row1 in result1:
#     with open('result_select_1.txt', 'a') as file:
#         file.write(str(row1)+ '\n')


sql = 'UPDATE country SET population = population + 100000 WHERE capital LIKE "%em"'
try :
    mycursor.execute(sql)
    mydb.commit()
except :
    mydb.rollback()

    
mycursor.execute('SELECT name FROM country ORDER BY population DESC')
res = mycursor.fetchall()
for el in res:
    with open ('result_name_pop.txt', 'a') as f:
        f.write(str(el) + '\n')

