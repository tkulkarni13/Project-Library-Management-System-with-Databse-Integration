from connect_mysql import connect_database

# Borrowed Book class which contains functions that manages data related to checked out books
class Borrowed_Book():
    # Add a new book that has been borrowed from library
    def add_borrowed_book(cursor, user_id, book_id, borrow_date, return_date):
        query = "INSERT INTO Borrowed_Books (user_id, book_id, borrow_date, return_date)\
            VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user_id, book_id, borrow_date, return_date))
        print("Borrowed book added.")
    
    # Remove a data point from the list of all borrwed books
    def remove_borrowed_book(cursor, bb_id):
        query = "DELETE FROM Borrowed_Books WHERE id = %s"
        cursor.execute(query, (bb_id,))
        print("Borrowed book deleted.")

    # Edit functions
    def edit_user_id(cursor, new_id, bb_id):
        query = "UPDATE Borrowed_Books SET user_id = %s WHERE id = %s"
        cursor.execute(query, (new_id, bb_id))
        print("User id updated.")
    
    def edit_book_id(cursor, new_id, bb_id):
        query = "UPDATE Borrowed_Books SET book_id = %s WHERE id = %s"
        cursor.execute(query, (new_id, bb_id))
        print("Book id updated.")

    def edit_borrow_date(cursor, new_date, bb_id):
        query = "UPDATE Borrowed_Books SET borrow_date = %s WHERE id = %s"
        cursor.execute(query, (new_date, bb_id))
        print("Borrow date updated.")
    
    def edit_return_date(cursor, new_date, bb_id):
        query = "Update Borrowed_Books SET return_date = %s WHERE id = %s"
        cursor.execute(query, (new_date, bb_id))
        print("Return date updated.")
    
    # Display details about one specfic instance of a borrowed book
    def view_borrowed_book_details (cursor, bb_id):
        query = "SELECT * FROM Borrowed_Books WHERE id = %s"
        cursor.execute(query, (bb_id,))
        bb_details = cursor.fetchone()

        if bb_details:
            print(bb_details)
        else:
            print("Invalid id entered.")
    
    # View all books that have been borrowed from the library
    def view_all_borrowed_books (cursor):
        query = "SELECT bb.id, u.id, u.name, u.library_id, bb.borrow_date, bb.return_date\
                from Borrowed_Books as bb, Users as u\
                where bb.user_id = u.id"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            for row in result:
                bb_id, u_id, u_name, u_library_id, borrow_date, return_date = row
                print(f"BB ID: {bb_id}, User ID: {u_id}, Name: {u_name}, Library ID: {u_library_id}, "\
                    f"Borrow Date: {borrow_date}, Return Date: {return_date}")
        else:
            print("No books have been checked out yet.")
    
# Main function for testing
def main():
        conn = connect_database()
        try:
            cursor = conn.cursor()
            # Borrowed_Book.remove_borrowed_book(cursor, 1)
            Borrowed_Book.view_all_borrowed_books(cursor)
            conn.commit()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()