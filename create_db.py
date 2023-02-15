import sqlite3
mybook=sqlite3.connect('book_info.db')
task=mybook.cursor()

flag=True

x=input('''
Enter 1 to add book to the database.
Enter 2 to delete book from the database.
Enter 3 to EXIT.
''')

task.execute('''CREATE TABLE books(name PRIMARY KEY,
author NOT NULL,
price FLOAT)''')

while flag==True:
    if x=='1':
        name=input('Enter the name of the book : ')
        author=input("Enter the name of author : ")
        price=float(input("Enter the price :"))
        operations.add(name,author,price)

    elif x=='2':
        name=input('Enter the name of the book to be deleted :')
        operations.delete(name)
    elif x=='3':
        flag=False
    else:
        print('Enter a valid input!')
        
