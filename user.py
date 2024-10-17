from connect_mysql import connect_database

# User class which stores function to manage all user data
class User:
    # Add user to database
    def add_user(cursor, name, library_id):
        query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
        cursor.execute(query, (name, library_id))
        print(f"{name} added as a user.")

    # Remove user from database
    def remove_user(cursor, user_id):
        query = "DELETE FROM Users WHERE id = %s"
        cursor.execute(query, (user_id,))
        print("User deleted.")
    
    # Edit name of specific user
    def edit_user_name(cursor, new_name, user_id):
        query = "UPDATE Users SET name = %s WHERE id = %s"
        cursor.execute(query, (new_name, user_id))
        print("Username updated.")
    
    # Edit library id of specific user
    def edit_user_library_id(cursor, new_library_id, user_id):
        query = "UPDATE Users SET library_id = %s WHERE id = %s"
        cursor.execute(query, (new_library_id, user_id))
        print("User's library id updated.")
    
    # View details of one user
    def view_user_details(cursor, user_id):
        query = "SELECT * FROM Users WHERE id = %s"
        cursor.execute(query, (user_id,))
        user_details = cursor.fetchone()

        if user_details:
            user_id, name, library_id = user_details
            print(f"User ID: {user_id}, Name: {name}, Library ID: {library_id}")
        else:
            print("Invalid user id entered.")
    
    # View all books borrowed by a specific user
    def view_user_borrowed_books(cursor, user_id):
        query = "select bb.id, u.id, u.name, u.library_id, b.id, b.title, bb.borrow_date, bb.return_date\
                from books as b, users as u, borrowed_books as bb\
                where b.id = bb.book_id and u.id = bb.user_id and u.id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()

        for row in result:
            bb_id, user_id, username, library_id, book_id, title, borrow_date, return_date = row
            print(f"BB ID: {bb_id}, User ID: {user_id}, Name: {username}, Library ID: {library_id}, "\
                  f"Book ID: {book_id}, Title: {title}, "\
                  f"Borrow Date: {borrow_date}, Return Date: {return_date}")
    
    # View all users stored in system
    def display_all_users(cursor):
        query = "SELECT * FROM Users"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            for row in result:
                user_id, name, library_id = row
                print(f"User ID: {user_id}, Name: {name}, Library ID: {library_id}")
        else:
            print("No users in system.")

# Main function for testing
def main():
    conn = connect_database()
    try:
        cursor = conn.cursor()

        # User.add_user(cursor, "User1", "0000000010")
        # User.remove_user(cursor, 1)
        # User.edit_user_name(cursor, "User 1", 2)
        # User.edit_user_library_id(cursor, "0000000001", 2)
        
        # User.view_user_details(cursor, 2)
        # User.view_user_borrowed_books(cursor, 2)
        User.display_all_users(cursor)

        conn.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()