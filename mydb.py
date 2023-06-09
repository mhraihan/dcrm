import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost', user='root', passwd=''
)

cursorObj = dataBase.cursor()

cursorObj.execute('CREATE DATABASE dcrm')

print("all done!")