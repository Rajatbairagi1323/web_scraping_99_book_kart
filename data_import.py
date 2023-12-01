import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password="7410",
    database='today_books'
)
cursor = conn.cursor()

# Create a table to store book details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS historical_fiction (
    isbn VARCHAR(255)PRIMARY KEY,
    name VARCHAR(255) PRIMARY KEY, 
    language VARCHAR(255),
    author VARCHAR(255),
    publisher VARCHAR(255),
    price FLOAT,
    pages INT,
    rating FLOAT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

# Insert data into the table from romance_books.csv
with open('/home/rajat/Desktop/web_scrap/historical_fiction.csv', 'r') as book_file:
    # Connect to the database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='7410',
        database='today_books'
    )
    cursor = conn.cursor()

    # Read each line from the file and insert into the table
    for line in book_file:
        data = line.strip().split(',')
        print(data)

        cursor.execute('''
            INSERT INTO historical_fiction (isbn, name, language, author, publisher, price, pages, rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


