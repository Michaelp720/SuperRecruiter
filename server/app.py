from db_utils import get_all_teams, get_team_by_id, get_capes_on_team, get_cape_by_id
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


def display_welcome(): #welcome page
  print("Welcome to Cape Recruiter! Setting/Ideas are from the world of Parahumans: you can start reading here https://parahumans.wordpress.com/ characters are OCs or AI generated")

def display_main_menu(): #main page
  print("[bold magenta]Main Menu[/]")
  print("1: Show all teams")
  print("2: Show solo capes")
  print("x: Exit")

def get_main_choice():
  return input("What would you like to do? ")

def display_all_teams(): #all teams page
  teams = get_all_teams()
  for team in teams:
    print(team)
  display_capes(get_team_choice())


def get_team_choice():
  return input("Which team would you like to see? ")

def display_capes(id): #team details page
  if id:
    displayed_team = display_team(id)
  else:
    displayed_team = "solo capes"
  print(get_capes_on_team(id))
  print("Cape ID: Show cape details")
  print(f"+: create a cape to join {displayed_team}")
  choice = get_cape_choice()
  if choice != "+":
    display_cape_details(choice, displayed_team)
  else:
    pass


def get_cape_choice():
  return input("Cape ID or +: ")

def display_team(id): #header for team details page
  team = get_team_by_id(id)
  print(f'{team.team_name} {team.allignment}')
  return team.team_name


def display_cape_details(id, team): #cape details page
  cape = get_cape_by_id(id)
  if cape.allignment == "Hero":
    if cape.team_id:
      cape_status = f"Hero with {team}"
    else:
      cape_status = f'Vigilante'
  elif cape.allignment == "Villain":
    if cape.team_id:
      cape_status = f"Villain with {team}"
    else:
      cape_status = f'Solo Villain'

  print(f'{cape.cape_name} | {cape.classification} | {cape_status}')
  print("1: change teams")
  print()


if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    
    display_welcome() #WELCOME PAGE
    print(Team.query.filter(Team.team_name == "Team Sunburst").first().id) #1 expected

    while True:
      display_main_menu() #MAIN PAGE
      choice = get_main_choice()
      if choice == "1":
        display_all_teams()
      elif choice == "2":
        display_capes(None)
      elif choice == "x":
        break
      




