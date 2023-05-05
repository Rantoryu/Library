import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="",
    database="library"
)
mycursor = mydb.cursor()

mycursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255),
        author VARCHAR(255),
        year INT(4)
    )
''')

def add_book(title, author, year):
    mycursor.execute('''
        INSERT INTO books (title, author, year)
        VALUES (%s, %s, %s)
    ''', (title, author, year))
    mydb.commit()
    print(mycursor.rowcount, "book added successfully")

def get_all_books():
    mycursor.execute('SELECT * FROM books')
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def update_book(id, title=None, author=None, year=None):
    query = 'UPDATE books SET '
    values = []
    if title:
        query += 'title = %s, '
        values.append(title)
    if author:
        query += 'author = %s, '
        values.append(author)
    if year:
        query += 'year = %s, '
        values.append(year)
    query = query[:-2] + ' WHERE id = %s'
    values.append(id)

    mycursor.execute(query, values)
    mydb.commit()

    if mycursor.rowcount == 0:
        print('No book found with id', id)
    else:
        print(mycursor.rowcount, 'book updated successfully')

def delete_book(id):
    mycursor.execute('DELETE FROM books WHERE id = %s', (id,))
    mydb.commit()

    if mycursor.rowcount == 0:
        print('No book found with id', id)
    else:
        print(mycursor.rowcount, 'book deleted successfully')

def main():
    while True:
        print('1. Add book')
        print('2. View all books')
        print('3. Update book')
        print('4. Delete book')
        print('5. Quit')
        choice = input('Enter your choice: ')

        if choice == '1':
            title = input('Enter title: ')
            author = input('Enter author: ')
            year = input('Enter year: ')
            add_book(title, author, year)
        elif choice == '2':
            get_all_books()
        elif choice == '3':
            id = input('Enter book id: ')
            title = input('Enter new title (press enter to skip): ')
            author = input('Enter new author (press enter to skip): ')
            year = input('Enter new year (press enter to skip): ')
            update_book(id, title, author, year)
        elif choice == '4':
            id = input('Enter book id: ')
            delete_book(id)
        elif choice == '5':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()