class Library:
    book_list = []
    def entry_book(self,new_book):
        self.book_list.append(new_book)


class Book(Library):
    def __init__(self,title,author,availability):
        __book_id = len(self.book_list) + 1
        self.__title = title
        self.__author = author
        self.__availability = availability

        add_book = {'ID':__book_id,'Title':title,'Author':author,'Availability':availability}
        self.entry_book(add_book)
    
    def borrow_book(self,id):
        for book in self.book_list:
            if book['ID'] == id:
                if book['Availability'] == 'Available':
                    print(f"Book '{book['Title']}' borrowed successfully.")
                    book['Availability'] = 'Not Available'
                else:
                    print('Trying to borrow a book that is already borrowed.')
    
    def return_book(self,id):
        for book in self.book_list:
            if book['ID'] == id:
                if book['Availability'] == 'Not Available':
                    print(f"Book '{book['Title']}' returned successfully.")
                    book['Availability'] = 'Available'
                else:
                    print('Trying to return a book that is not borrowed.')

    def view_book_info(self):
        print('Library All Books:')
        for book in self.book_list:
            print(f"ID : {book['ID']}, Title : {book['Title']}, Author : {book['Author']}, Availability : {book['Availability']}")

    def menu_driven_system(self):
        while True:
            text ="""
                -----Welcome to the Library-------
                Choose options:
                1. View All Books
                2. Borrow Book
                3. Return Book
                4. Exit.
                """
            print(text)
            option = int(input('Enter your choice: '))
            if option == 1:
                self.view_book_info()
            elif option == 2:
                id = int(input('Enter book ID to borrow: '))
                is_available = False
                for bookId in self.book_list:
                    if bookId['ID'] == id:
                        is_available = True
                        break
                if(is_available == True):
                    self.borrow_book(id)
                else:
                    print('Invalid book ID')
            elif option == 3:
                id = int(input('Enter book ID to return: '))
                is_available = False
                for bookId in self.book_list:
                    if bookId['ID'] == id:
                        is_available = True
                        break
                if(is_available == True):
                    self.return_book(id)
                else:
                    print('Invalid book ID')
            elif option == 4:
                break


# Demo Book Data
insert = Book('Computer Programming','Tamim Sahariar','Available')
insert = Book('Programming Contest','Mahbubul Hasan','Available')
insert = Book('Paradoxical Sajid','Arif Azad','Available')
insert = Book('Double Standard','Samsul Arafin','Available')
insert = Book('ABC English Grammer','Jahurul Islam','Available')


insert.menu_driven_system()
