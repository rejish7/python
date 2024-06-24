import mysql.connector

# establish the database connection
cnx = mysql.connector.connect(
    user='root', 
    password='Rejish@1',
    host='localhost',
    database='python_database'
)

# create a cursor object
cursor = cnx.cursor()

# SQL query string
sql_query = ("INSERT INTO Tables "
             "(column1, column2) "
             "VALUES (%s, %s)")

# data to be inserted
data = ('value1', 'value2')

# execute the query
cursor.execute(sql_query, data)

# commit the transaction
cnx.commit()

# close the cursor and connection
cursor.close()
cnx.close()
