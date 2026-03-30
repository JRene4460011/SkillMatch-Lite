import os
import sys
import time
import database
from users import (add_user, view_users, update_user, delete_user)
from jobs import (add_job, view_jobs, update_job, delete_job)
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
    print("1.  Add User")
    print("2.  View Users")
    print("3.  Update User")
    print("4.  Delete User")
    print("5.  Add Job")
    print("6.  View Jobs")
    print("7.  Update Job")
    print("8.  Delete Job")
    print("9.  Match Skills")
    print("10. Exit")
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
        choice = input("\nEnter your choice (1-10): ").strip()
        if choice in [str(i) for i in range(1, 11)]:
            return choice
        print("Invalid. Please enter a number from 1 to 10.")

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
                anotheruser = input("\nAdd another user? (y/n): ").strip().lower()
                if anotheruser not in ["y", "n"]:
                    print("The acceptable values are 'y' or 'n'.")
                    time.sleep(3)
                    break
                if anotheruser != "y":
                    break

        elif choice == "2":
            view_users()
            input("\nPress Enter to continue...")

        elif choice == "3":
            update_user()
            input("\nPress Enter to continue...")

        elif choice == "4":
            delete_user()
            input("\nPress Enter to continue...")

        elif choice == "5":
            while True:
                add_job()
                anotherjob = input("\nAdd another job? (y/n): ").strip().lower()
                if anotherjob not in ["y", "n"]:
                    print("The acceptable values are 'y' or 'n'.")
                    time.sleep(3)
                    break
                if anotherjob != "y":
                    break

                # if input("\nAdd another job? (y/n): ").strip().lower() != "y":
                #     break

        elif choice == "6":
            view_jobs()
            input("\nPress Enter to continue...")

        elif choice == "7":
            update_job()
            input("\nPress Enter to continue...")

        elif choice == "8":
            delete_job()
            input("\nPress Enter to continue...")

        elif choice == "9":
            match_user()
            input("\nPress Enter to continue...")

        elif choice == "10":
            if input("\nAre you sure you want to exit? (y/n): ").strip().lower() == "y":
                print("\nThank you for using SkillMatch Lite! Good luck!")
                sys.exit(0)

if __name__ == "__main__":
    main()
