from Utils import Database

USER_CHOICE = '''
Enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit

Your choice :'''

def menu():
    try:
        Database.create_book_table()
    except:
        pass
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command, please enter valid command.")
        
        
        user_input = input(USER_CHOICE)


# def prompt_add_book() ask for book name and author
# def list_books() show all the books in our list
# def prompt_read_book() ask for book name and change it to *read* in our list
# def prompt_delete_book() ask for book name and remove book from list


def prompt_add_book():
    name = input("Enter the new book name")
    author = input("Enter the author name")
    Database.add_book(name,author)


def list_books():
    books = Database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input("enter the name of book you finished")
    Database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of book you want to delete")
    Database.delete_book(name)

menu()