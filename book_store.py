import operations
print('!!WELCOME TO MY BOOK STORE!!')
flag=True
while flag==True:
    print('''
Enter 1 to list all the titles of books.
Enter 2 to buy books.
Enter 3 to QUIT.''')

    x=input('\n')

    if x=='1':
        operations.list()
        print('\n')


    elif x=='2':
        name=input('Enter the name of the book : ')

        operations.info(name)

        if operations.stop==False:
            quantity=int(input('Enter the number of copies : '))
            total=quantity*operations.getprice(name)
            print('Your total is Rs.'+str(total))

        response=input('DO you wish to buy more books?(Y/N)  ')
        if response.lower()=='n':
            flag=False
    elif x=='3':
        flag=False
    else:
        print('Unknown input. Please enter a valid input.')

            
