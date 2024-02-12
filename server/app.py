from config import app, migrate
from models import db
from rich import print

# Tasks:
# 1. welcome page- show all teams, show all solo capes
# 2. See all capes on a team or solo capes
# 3. See cape details
# 4. Change a cape's team
# 5. Add a cape to this team (or create solo cape)
# 6. Add a team


def display_welcome():
  print("Welcome to Cape Recruiter! Setting/Ideas are from the world of Parahumans: you can start reading here https://parahumans.wordpress.com/ characters are OCs or AI generated")

def display_main_menu():
  pass


if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    
    display_welcome()
    while True:
      display_main_menu()
      break
