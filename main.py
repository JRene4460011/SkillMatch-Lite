import os
import sys
import database
from add_user import add_user
from add_job import add_job
from view_users import view_users
from view_jobs import view_jobs
from match import match_user

# Clears the terminal screen to keep the interface clean between menu actions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Prints the app name and tagline at the top of every screen
def show_header():
    print("=" * 50)
    print(" SKILLMATCH LITE")
    print(" match your skills to the right job")
    print("=" * 50)

# Prints the list of available actions the user can choose from
def show_menu():
    print("\n-- MAIN MENU --")
    print("1. Add a user")
    print("2. Add a job")
    print("3. View all users")
    print("4. View all jobs")
    print("5. Match user to job")
    print("6. Exit")
    print("-" * 30)

# Sets up the database and retries if MySQL is not running yet
def setup_with_retry():
    while True:
        try:
            database.setup_database()
            print("Database ready!")
            break
        except Exception as e:
            print(f"\nConnection failed: {e}")
            print("Make sure MySQL is running.")
            if input("Retry? (y/n): ").strip().lower() != "y":
                sys.exit(0)

# Keeps asking for input until the user enters a valid number from 1 to 6
def get_valid_choice():
    while True:
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        print("Invalid. Please enter a number from 1 to 6.")

# Runs the app — sets up the database then starts the main menu loop
def main():
    print("\nSetting up the database...")
    setup_with_retry()

    while True:
        clear_screen()
        show_header()
        show_menu()

        choice = get_valid_choice()

        if choice == "1":
            while True:
                add_user()
                if input("\nAdd another user? (y/n): ").strip().lower() != "y":
                    break

        elif choice == "2":
            while True:
                add_job()
                if input("\nAdd another job? (y/n): ").strip().lower() != "y":
                    break

        elif choice == "3":
            view_users()
            input("\nPress Enter to continue...")

        elif choice == "4":
            view_jobs()
            input("\nPress Enter to continue...")

        elif choice == "5":
            match_user()
            input("\nPress Enter to continue...")

        elif choice == "6":
            if input("\nAre you sure you want to exit? (y/n): ").strip().lower() == "y":
                print("\nThank you for using SkillMatch Lite! Good luck!")
                sys.exit(0)

if __name__ == "__main__":
    main()
