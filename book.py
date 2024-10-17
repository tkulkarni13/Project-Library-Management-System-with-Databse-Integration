from connect_mysql import connect_database

# Book class contains functions to manage book data
class Book:
    # Add a book to library system
    def add_book(cursor, title, author_id, isbn, publication_date):
        query = "INSERT INTO Books (title, author_id, isbn, publication_date)\
            VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (title, author_id, isbn, publication_date))
        print(f"{title} added as a book.")
    
    # Remove a book from the system
    def remove_book(cursor, book_id):
        query = "DELETE FROM Books WHERE id = %s"
        cursor.execute(query, (book_id,))
        print("Book deleted.")
    
    # Edit functions
    def edit_book_title(cursor, new_title, book_id):
        query = "UPDATE Books SET title = %s WHERE id = %s"
        cursor.execute(query, (new_title, book_id))
        print("Book title updated.")

    def edit_book_author_id(cursor, new_author_id, book_id):
        query = "UPDATE Books SET author_id = %s WHERE id = %s"
        cursor.execute(query, (new_author_id, book_id))
        print("Book author updated.")
    
    def edit_book_isbn(cursor, new_isbn, book_id):
        query = "UPDATE Books SET isbn = %s WHERE id = %s"
        cursor.execute(query, (new_isbn, book_id))
        print("Book isbn updated.")
    
    def edit_book_publication_date(cursor, new_publication_date, book_id):
        query = "UPDATE Books SET publication_date = %s WHERE id = %s"
        cursor.execute(query, (new_publication_date, book_id))
        print("Book publication date updated.")
    
    # Checks if a book is available for checkout
    def is_available(cursor, book_id):
        query = "SELECT availability FROM Books WHERE id = %s"
        cursor.execute(query, (book_id,))
        result = cursor.fetchone()

        return result[0] == 1

    # Checkout a book if it is available
    def checkout_book(cursor, borrow_date, user_id, book_id):
        if Book.is_available(cursor, book_id):
            query = "UPDATE Books SET availability = 0 WHERE id = %s"
            cursor.execute(query, (book_id,))

            query = "INSERT INTO Borrowed_Books (user_id, book_id, borrow_date, return_date)\
                VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (user_id, book_id, borrow_date, None))

            print("Book checked out.")
        else:
            print("Book is unavailble to be checked out.")

    # Checkin a book if it is unavailable
    def checkin_book(cursor, return_date, book_id, borrowed_book_id):
        if Book.is_available(cursor, book_id):
            print("Book is available, cannot be checked in.")
        else:
            query = "UPDATE Books SET availability = 1 WHERE id = %s"
            cursor.execute(query, (book_id,))

            query = "UPDATE Borrowed_Books SET return_date = %s WHERE id = %s"
            cursor.execute(query, (return_date, borrowed_book_id))

            print("Book checked in.")

    # Search for a book bases on its title or isbn
    def search_books(cursor, search):
        query = "SELECT * FROM Books WHERE title LIKE %s or isbn LIKE %s"
        arg = ('%' + search + '%')
        cursor.execute(query, (arg, arg))
        result = cursor.fetchall()

        if result:
            for row in result:
                Book.print_book_details(cursor, row)
        else:
            print("No books match search.")
    
    # Helper function to format information
    def print_book_details(cursor, book_details):
        book_id, title, author_id, isbn, publication_date, availability = book_details

        query = "SELECT name FROM Authors WHERE id = %s"
        cursor.execute(query, (author_id,))
        author_name = cursor.fetchone()[0]

        print(f"Book ID: {book_id}, Title: {title}, Author ID: {author_id}, Author: {author_name}, "\
              f"ISBN = {isbn}, Publication Date: {publication_date}, Availability: {availability}")
        
    # View information about one book
    def view_book_details(cursor, book_id):
        query = "SELECT * FROM Books WHERE id = %s"
        cursor.execute(query, (book_id,))
        book_details = cursor.fetchone()
        
        if book_details:
            Book.print_book_details(cursor, book_details)
        else:
            print("Invalid book_id entered.")

    # View information about all books in library system
    def display_all_books(cursor):
        query = "SELECT * FROM Books"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            for row in result:
                Book.print_book_details(cursor, row)

        else:
            print("No books in system.")

# Main function for testing
def main():
    conn = connect_database()
    try:
        cursor = conn.cursor()
        # Book.add_book(cursor, "Book1", 6, "1231231230123", "2023-01-01")
        # Book.edit_book_title(cursor, "Book 1", 2)
        # Book.search_books(cursor, "123")
        # Book.checkout_book(cursor, "2023-02-11", 2, 2)
        # Book.checkin_book(cursor, "2023-02-10", 2, 1)

        Book.display_all_books(cursor)

        conn.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()