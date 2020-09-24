import mysql.connector

def DataUpdate(first_name):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    mycursor=mydb.cursor()


    sql = "CREATE TABLE customers (first_name VARCHAR(255));"
    sql='INSERT INTO customers (first_name) VALUES ("{0}");'.format(first_name)
    # val = ("jack")
    mycursor.execute(sql)

    mydb.commit()

    #print(mycursor.rowcount, "record inserted.")

