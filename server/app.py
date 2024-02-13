from db_utils import get_all_teams
from config import app, migrate
from models import Cape, Team, db

#from rich import print

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
  print("[bold magenta]Main Menu[/]")
  print("1: Show all teams")
  print("2: Show solo capes")
  print("x: Exit")

def get_main_choice():
  return input("What would you like to do? ")

def display_all_teams():
  #print(db.session.query(Team).filter(Team.team_name == "Team Sunburst")) #1 expected
  teams = get_all_teams()
  for team in teams:
    print(team)
  get_team_choice()

def get_team_choice():
  return input("Which team would you like to see? ")

def display_solo_capes():
  print("SOLO CAPES")
  print("Cape ID: Show cape details")
  print("+: create a cape")

def get_cape_choice():
  return input("Cape ID or +: ")

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    
    display_welcome() #WELCOME PAGE
    while True:
      display_main_menu() #MAIN PAGE
      choice = get_main_choice()
      if choice == "1":
        display_all_teams()
      elif choice == "2":
        display_solo_capes()
      elif choice == "x":
        break
      




