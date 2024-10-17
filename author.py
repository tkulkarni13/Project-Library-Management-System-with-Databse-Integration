from connect_mysql import connect_database

# Author class which stores helpful functions for managing author data
class Author:
    # Add author to system
    def add_author(cursor, name, biography):
        query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"
        cursor.execute(query, (name, biography))
        print(f"{name} added as an author.")

    # Remove author from system
    def remove_author(cursor, author_id):
        query = "DELETE FROM Authors WHERE id = %s"
        cursor.execute(query, (author_id,))
        print("Author deleted.")

    # Edit functions
    def edit_author_name(cursor, new_name, author_id):
        query = "UPDATE Authors SET name = %s WHERE id = %s"
        cursor.execute(query, (new_name, author_id))
        print("Author name updated.")
    
    def edit_author_biography(cursor, new_biography, author_id):
        query = "UPDATE Authors SET biography = %s WHERE id = %s"
        cursor.execte(query, (new_biography, author_id))
        print("Author biography updated.")

    # View information about one author
    def view_author_details(cursor, author_id):
        query = "SELECT * FROM Authors WHERE id = %s"
        cursor.execute(query, (author_id,))
        author_details = cursor.fetchone()
        
        if author_details:
            author_id, name, biography = author_details
            print(f"Author ID: {author_id}, Name: {name}, Biography: {biography}")
        else:
            print("Invalid author id entered.")

    # Display all authors stored in database
    def display_all_authors(cursor):
        query = "SELECT * FROM Authors"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            for row in result:
                author_id, name, biography = row
                print(f"Author ID: {author_id}, Name: {name}, Biography: {biography}")
        else:
            print("No authors in system.")

# Main method for testing
def main():
    conn = connect_database()
    try:
        cursor = conn.cursor()
        # Author.add_author(cursor, "Author1", "This is author.")
        # Author.remove_author(cursor, 2)
        # Author.edit_author_name(cursor, "Author 1", 6)

        # Author.view_author_details(cursor, 6)
        Author.display_all_authors(cursor)

        conn.commit()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()