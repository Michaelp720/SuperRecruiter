from db_utils import get_all_teams, get_team_by_id, get_capes_on_team, get_cape_by_id, delete_cape, change_capes_team
from config import app, migrate
from models import Cape, Team, db

from rich import print

# Tasks:
# 1. welcome page- show all teams, show all solo capes
# 2. See all capes on a team or solo capes
# 3. See cape details
# 4. Change a cape's team
# 5. Add a cape to this team (or create solo cape)
# 6. Add a team


def display_welcome(): #welcome page
  print("Welcome to [bold #f3cf22]Cape Recruiter![/]")
  f= open ('edited_capes.txt','r')
  print(''.join([line for line in f]))
  print("Setting/Ideas are from the world of Parahumans: you can start reading here https://parahumans.wordpress.com/")
  print("Characters are OCs or AI generated")
  print("")

def display_main_menu(): #main page
  print("[bold #f3cf22]Main Menu[/]")
  print("[bold cyan]1[/]: Show all teams")
  print("[bold cyan]2[/]: Show solo capes")
  print("[bold cyan]x[/]: Exit")

def get_main_choice():
  return input("What would you like to do? ")

def display_all_teams(): #all teams page
  teams = get_all_teams()
  for team in teams:
    print(team)
  display_capes(get_team_choice())


def get_team_choice():
  return input("Which team would you like to see? ")

def display_capes(id): #team details page/solo capes
  if id:
    displayed_team = display_team(id)
  else:
    displayed_team = "solo capes"
  capes_on_team = get_capes_on_team(id)
  for cape in capes_on_team:
    print(cape)
  print("Cape ID: Show cape details")
  print(f"+: create a cape to join {displayed_team}")
  print("other: return to main menu")
  choice = get_cape_choice()
  if choice == "+":
    print("Create cape placeholder")
  else:
    display_cape_details(choice, displayed_team, id) #make error not cause exit?


def get_cape_choice():
  return input("Cape ID or +: ")

def display_team(id): #header for team details page
  team = get_team_by_id(id)
  print(f'{team.team_name} {team.allignment}')
  return team.team_name


def display_cape_details(id, team, team_id): #cape details page
  cape = get_cape_by_id(id)
  if cape.allignment == "Heroic":
    if cape.team_id:
      cape_status = f"Hero with {team}"
    else:
      cape_status = f'Vigilante'
  elif cape.allignment == "Villainous":
    if cape.team_id:
      cape_status = f"Villain with {team}"
    else:
      cape_status = f'Solo Villain'

  print(f'{cape.cape_name} | {cape.classification} | {cape_status}')
  if cape.team_id:
    print(f"1: back to {team}")
  else:
    print("1: back to solo capes")
  print(f"2: assign {cape.cape_name} to new team")
  print(f"-: delete {cape.cape_name} permanently")
  print("other: return to main menu")
  choice = get_cape_dets_choice()
  if choice == "1":
    display_capes(team_id)
  elif choice == "2":
    #print("Update placeholder")
    change_capes_team(cape)
  elif choice == "-":
    delete_cape(cape)

def get_cape_dets_choice():
  return input("Selection: ")

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    
    display_welcome() #WELCOME PAGE
    #print(Team.query.filter(Team.team_name == "Team Sunburst").first().id) #1 expected

    while True:
      display_main_menu() #MAIN PAGE
      choice = get_main_choice()
      if choice == "1":
        display_all_teams()
      elif choice == "2":
        display_capes(None)
      elif choice == "x":
        break
      




