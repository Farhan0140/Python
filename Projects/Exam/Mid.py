
class Library:
    book_list = list()

    @classmethod
    def entry_book(self, book_obj):
        self.book_list.append( book_obj )


class Book:
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self.__author = author
        self._availability = True

        Library.entry_book( self )


    @classmethod
    def borrow_book(self, book_id):

        for books in Library.book_list:
            if books._book_id == book_id:
                if books._availability:
                    books._availability = False
                    print(' * Book borrowed successfully * ')
                    return
                else:
                    print(' * Book Not Available * ')
                    return
        raise ValueError(" * Book not found * ")
    

    @classmethod
    def return_book(self, book_id):
        for books in Library.book_list:
            if books._book_id == book_id:
                if books._availability == False:
                    books._availability = True
                    print(' * Book return successfully * ')
                    return
                else:
                    print(' * This Book was never borrowed * ')
                    return
        raise ValueError(" * Book not found * ")


    @classmethod
    def view_book_info(self):
        print(' \n* ------------------- *\n ' )
        for books in Library.book_list:
            s = 'Available'
            if not books._availability:
                s = 'Not Available'
                    
            print(f'Book id: {books._book_id}  Title: {books._title}  Author: {books.__author}  Availability: {s}')
            print('* ------------------- *   ' )






Book(101, 'DSA', 'Farhan Nadim')
Book(102, 'DBMS', 'Niamot')
Book(103, 'AI', 'Niamul haque')
Book(104, 'CN', 'Mr. Baten')
Book(105, 'LPS', 'Rifat')
Book(106, 'Java', 'Rahat')





print(' \n* ---------- Welcome To The Library --------- *\n ' )
while True:
    print('1. View All Books\n2. Borrow Book\n3. Return Book\n4. Exit')
    try:
        chk = int(input( '---> ' ))
        if chk == 1:
            Book.view_book_info()
        elif chk == 2:
            b_id = int(input('Enter Book Id: '))
            bl = Book.borrow_book(b_id)
        elif chk == 3:
            b_id = int(input('Enter Book Id: '))
            bl = Book.return_book(b_id)
        elif chk == 4:
            break
    except ValueError:
        print(f'Error: {ValueError}')
    except Exception:
        print(f"An unexpected error occurred: {Exception}")


     