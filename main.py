from book import Book
from user import User
from author import Author
from borrowed_book import Borrowed_Book
from connect_mysql import connect_database

# Functions to print instructions to the user depending on which part of the application they are using
def print_main_menu_instruction():
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. View all borrowed books")
    print("5. Quit")

def print_book_operations():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    print("6. Remove a book")

def print_user_operations():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. View user's borrowed books")
    print("4. Display all users")
    print("5. Remove a user")

def print_author_operations():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    print("4. Remove an author")

# Main method which handles the command-line interface and interaction with user
def main():
    conn = connect_database()
    try:
        cursor = conn.cursor()
        print_main_menu_instruction() # Print options for user

        while True: # Loop until terminated by user
            # try except block to make sure user input is an integer - This shows up everytime we use 'int(input("..."))'
            try:
                user_input_1 = int(input("Please select a number from the menu above: "))
            except ValueError:
                print("Please enter a valid digit.")
            else:
                # Book Operations
                if (user_input_1 == 1):
                    print_book_operations() # Print options for user
                    try:
                        user_input_2 = int(input("Please select a number from the options above: "))
                    except ValueError:
                        print("Please enter a valid digit")
                        print_main_menu_instruction()
                    else:
                        # Add a new book
                        if (user_input_2 == 1):
                            title = input("Title: ")
                            author = input("Author ID: ")
                            isbn = input("ISBN: ")
                            publication_date = input("Publication Date: ")
                            Book.add_book(cursor, title, author, isbn, publication_date)
                            conn.commit()
                            print_main_menu_instruction()

                        # Borrow a book
                        elif (user_input_2 == 2):
                            book_id = input("Book ID: ")
                            user_id = input("User ID: ")
                            borrow_date = input("Borrow date: ")
                            Book.checkout_book(cursor, borrow_date, user_id, book_id)
                            conn.commit()
                            print_main_menu_instruction()
                        
                        # Return a book
                        elif (user_input_2 == 3):
                            book_id = input("Book ID: ")
                            bb_id = input("Borrowed book id: ")
                            return_date = input("Return date: ")
                            Book.checkin_book(cursor, return_date, book_id, bb_id)
                            conn.commit()
                            print_main_menu_instruction()

                        # Search for a book
                        elif (user_input_2 == 4):
                            search = input("Search for a book by its title or isbn: ")
                            Book.search_books(cursor, search)
                            print_main_menu_instruction()

                        # Display all books
                        elif (user_input_2 == 5):
                            Book.display_all_books(cursor)
                            print_main_menu_instruction()
                        
                        # Remove a book from the library system
                        elif (user_input_2 == 6):
                            book_id = input("Book ID: ")
                            Book.remove_book(cursor, book_id)
                            conn.commit()
                            print_main_menu_instruction()
                        
                        else:
                            print("Please enter a valid digit.")
                            print_main_menu_instruction()

                # User Operations
                elif (user_input_1 == 2):
                    print_user_operations()
                    try:
                        user_input_2 = int(input("Please select a number from the options above: "))
                    except ValueError:
                        print("Please enter a valid digit.")
                        print_main_menu_instruction()
                    else:
                        # Add a new user
                        if (user_input_2 == 1):
                            name = input("Name: ")
                            library_id = input("Library ID: ")
                            User.add_user(cursor, name, library_id)
                            conn.commit()
                            print_main_menu_instruction()

                        # View user details
                        elif (user_input_2 == 2):
                            user_id = input("User ID: ")
                            User.view_user_details(cursor, user_id)
                            print_main_menu_instruction()

                        # View user's borrowed books
                        elif (user_input_2 == 3):
                            user_id = input("User ID: ")
                            User.view_user_borrowed_books(cursor, user_id)
                            print_main_menu_instruction()

                        # Display all users
                        elif (user_input_2 == 4):
                            User.display_all_users(cursor)
                            print_main_menu_instruction()
                        
                        # Remove a user
                        elif (user_input_2 == 5):
                            user_id = input("User ID: ")
                            User.remove_user(cursor, user_id)
                            conn.commit()
                            print_main_menu_instruction()

                        else:
                            print("Please enter a valid digit.")
                            print_main_menu_instruction()

                # Author Operations
                elif (user_input_1 == 3):
                    print_author_operations()
                    try:
                        user_input_2 = int(input("Please select a number from the options above: "))
                    except ValueError:
                        print("Please enter a valid digit.")
                        print_main_menu_instruction()
                    else:
                        # Add a new author
                        if (user_input_2 == 1):
                            name = input("Name: ")
                            biography = input("Biography: ")
                            Author.add_author(cursor, name, biography)
                            conn.commit()
                            print_main_menu_instruction()
                        
                        # View author details
                        elif (user_input_2 == 2):
                            author_id = input("Author ID: ")
                            Author.view_author_details(cursor, author_id)
                            print_main_menu_instruction()

                        # Display all authors
                        elif (user_input_2 == 3):
                            Author.display_all_authors(cursor)
                            print_main_menu_instruction()

                        # Remove author
                        elif (user_input_2 == 4):
                            author_id = input("Author ID: ")
                            Author.remove_author(cursor, author_id)
                            conn.commit()
                            print_main_menu_instruction()

                        else:
                            print("Please enter a valid digit")
                            print_main_menu_instruction()

                elif (user_input_1 == 4):
                    Borrowed_Book.view_all_borrowed_books(cursor)
                    print_main_menu_instruction()

                # Exit the loop and end the program
                elif (user_input_1 == 5):
                    break

                else:
                    print("Please enter a valid digit.")
                    print_main_menu_instruction()
        conn.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()