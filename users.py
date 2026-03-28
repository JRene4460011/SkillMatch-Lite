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

if __name__ == "__main__":
    add_user()
