from database import get_connection

# Collects a new user's name and skills from the terminal and saves them to the database
def add_user():
    print("\nADD NEW USER")
    name = input("Enter your name: ").strip()
    skills = input("Enter your skills separated by commas: ").strip()

    # Stop early if the user left either field empty
    if not name or not skills:
        print("Name and skills cannot be empty.")
        return

    # We do not accept numbers only for the name and skills.
    if name.strip().isdigit() or skills.strip().isdigit():
        print("Name and skills cannot be numbers only.")
        return

    # Use the shared connection from database.py instead of repeating connection code
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Insert the new user into the users table
        cursor.execute("INSERT INTO users (name, skills) VALUES (%s, %s)", (name, skills))
        conn.commit()
        print(f"\n{name} added successfully!")
    except Exception as e:
        # Print the error instead of crashing the whole program
        print(f"Something went wrong: {e}")
    finally:
        # Always close the cursor and connection even if something goes wrong
        cursor.close()
        conn.close()

def view_users():
    print("\nALL REGISTERED USERS")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, name, skills FROM users")
        users = cursor.fetchall()

        if not users:
            print("No users found.")
        else:
            print("-" * 40)
            print(f"{'ID':<5} {'Name':<20} {'Skills'}")
            print("-" * 40)
            for user in users:
                print(f"{user[0]:<5} {user[1]:<20} {user[2]}")
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        cursor.close()
        conn.close()

   
def delete_user():
    print("\nDELETE USER")
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Show all users so the person can pick which one to delete
        cursor.execute("SELECT id, name, skills FROM users")
        users = cursor.fetchall()
        if not users:
            print("No users found.")
            return
        print("-" * 40)
        for user in users:
            print(f"  ID: {user[0]} | NAME: {user[1]} | SKILLS: {user[2]}")
        print("-" * 40)
        try:
            user_id = int(input("Enter user ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return
        # Check that the user actually exists before trying to delete
        cursor.execute("SELECT id, name FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if not user:
            print(f"No user found with ID {user_id}.")
            return
        # Confirm before deleting
        confirm = input(f"Are you sure you want to delete '{user[1]}'? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Deletion cancelled.")
            return
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        print(f"Deleted user '{user[1]}' with ID {user_id}.")
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        cursor.close()
        conn.close()
def update_user():
    print("\nUPDATE USER")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, name, skills FROM users")
        users = cursor.fetchall()

        if not users:
            print("No users found.")
            return

        print("-" * 40)
        for user in users:
            print(f"  ID: {user[0]} | NAME: {user[1]} | SKILLS: {user[2]}")
        print("-" * 40)

        try:
            user_id = int(input("Enter user ID to update: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        cursor.execute("SELECT id, name, skills FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        if not user:
            print(f"No user found with ID {user_id}.")
            return

        print(f"\nUPDATING USER: {user[1]}")
        new_name = input(f"Enter new name (leave blank to keep '{user[1]}'): ").strip()
        new_skills = input(f"Enter new skills (leave blank to keep '{user[2]}'): ").strip()

        if not new_name and not new_skills:
            return

        updated_name = new_name if new_name else user[1]
        updated_skills = new_skills if new_skills else user[2]

        cursor.execute(
            "UPDATE users SET name = %s, skills = %s WHERE id = %s",
            (updated_name, updated_skills, user_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        cursor.close()
        conn.close()
