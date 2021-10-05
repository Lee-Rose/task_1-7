import mysql.connector
import data_country

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='88881111',
    database='ex10db'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE IF NOT EXISTS country (name VARCHAR(100), capital VARCHAR(100), population INTEGER)')
mycursor.execute('SHOW TABLES')

sqlFormula = 'INSERT INTO country (name, capital, population) VALUES (%s, %s, %s)'
for item in data_country.country_list:
    mycursor.execute(sqlFormula, item)
    mydb.commit()
