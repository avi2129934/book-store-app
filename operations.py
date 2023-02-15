import sqlite3
mybook=sqlite3.connect('book_info.db')
task=mybook.cursor()


stop=False
def info(name):
    task.execute('select * from books where name=?;',(name,))
    book=task.fetchone()
    global stop
    if book==None:
        print("Sorry, looks like we are out of stock on that one.")
        stop=True
    else:
        print(book)
    
def add(name,author,price):
    task.execute("insert into books(name,author,price) values (?,?,?)",(name,author,price))
    mybook.commit()
    print("Book Added successfully!")

def update(name,author,price,old_name):
    task.execute("update books set name=?, author=?, price=? where name=?",(name,author,price,old_name))
    mybook.commit()
    print('Record updated successfully.')

def delete(x):
    task.execute("delete from books where name=?;",(x,))
    resp=input("Enter Y to confirm delete.")
    if resp.lower()=='y':
        mybook.commit()
        print('Book deleted successfully from database.')
    else:
        mybook.rollback()

def getprice(name):
    task.execute("select price from books where name=?",(name,))
    cost=task.fetchone()
    price=cost[0]
    return price

def list():
    bklist=[]
    task.execute("select name from books")
    title=task.fetchall()
    for book in title:
        bklist.append(book[0])
        if book==None:
            break
    print(bklist)
