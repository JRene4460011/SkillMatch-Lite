from database import setup_database
from users import *
from jobs import *
from match import match_skills

# I think we can put our terminal option menus here.
def menu():
    pass

if __name__ == "__main__":
    setup_database()
    menu()