from db_utils import get_all_teams, get_team_by_id, get_capes_on_team, get_cape_by_id, delete_cape, change_capes_team, create_cape, create_team, get_cape_status
from config import app, migrate
from models import Cape, Team, db
from rich import print
from rich.text import Text
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

from styles import page_heading_style, cape_panel

# Tasks:
# 1. welcome page- show all teams, show all solo capes
# 2. See all capes on a team or solo capes
# 3. See cape details
# 4. Change a cape's team
# 5. Add a cape to this team (or create solo cape)
# 6. Add a team

console = Console()

def display_welcome(): #welcome page
  console.print("Welcome to Cape Recruiter!", justify = "center", style = page_heading_style)
  print("")
  f= open ('edited_capes.txt','r')
  print(''.join([line for line in f]))
  print("Setting/Ideas are from the world of Parahumans: you can start reading here https://parahumans.wordpress.com/")
  print("Characters are OCs or AI generated")
  print("")

def display_main_menu(): #main page
  console.print("Main Menu", style = page_heading_style)
  print("[bold green]1[/]: Show all teams")
  print("[bold green]2[/]: Show solo capes")
  print("[bold green]3[/]: Show all capes")
  print("[bold green]+[/]: Create new team") #will become recruiting game
  print("[bold green]x[/]: Exit")

def get_main_choice():
  return input("What would you like to do? ")

def display_all_teams(): #all teams page
  teams = get_all_teams()
  for team in teams:
    print(team)  ##################################
  display_capes(get_team_choice())


def get_team_choice():
  return input("Which team would you like to see? ")

def display_capes(id): #team details page/solo capes
  if not id:
    displayed_team = "solo capes"
    is_all = False
  elif id == "All":
    displayed_team = "all capes"
    is_all = True
  else:
    displayed_team = display_team(id)
    is_all = False
    
  capes_on_team = get_capes_on_team(id)

  cape_renders = [Panel(cape_panel(cape, is_all)) for cape in capes_on_team]
  console.print(Columns(cape_renders))
  # for cape in capes_on_team:
  #   print(cape)   #######################################

  print("[bold green]Cape ID[/]: Show cape details")
  print(f"[bold green]+[/]: create a cape to join {displayed_team}")
  print("[bold green]x[/]: return to main menu")
  print("[bold green]other[/]: quit app") #bug? or feature ;)
  choice = get_cape_choice()
  if choice == "+":
    display_capes(create_cape(id))
  elif choice == "x":
    start_main_menu()
  else:
    display_cape_details(choice, displayed_team, id)


def get_cape_choice():
  return input("Cape ID or +: ")

def display_team(id): #header for team details page
  team = get_team_by_id(id)
  print(f'{team.team_name} {team.allignment}')
  return team.team_name


def display_cape_details(id, team, team_id): #cape details page
  cape = get_cape_by_id(id)

  cape_status = get_cape_status(cape.allignment, team, cape.team_id)

  print(f'{cape.cape_name} | {cape.classification} | {cape_status}')
  print(f"1: back to {team}")
  print(f"2: assign {cape.cape_name} to new team")
  print(f"-: delete {cape.cape_name} permanently")
  print("other: return to main menu")
  choice = get_cape_dets_choice()
  if choice == "1":
    display_capes(team_id)
  elif choice == "2":
    change_capes_team(cape)
  elif choice == "-":
    delete_cape(cape)
  else:
    start_main_menu()

def get_cape_dets_choice():
  return input("Selection: ")

def start_main_menu():
  while True:
      display_main_menu() #MAIN PAGE
      choice = get_main_choice()
      if choice == "1":
        display_all_teams()
      elif choice == "2":
        display_capes(None)
      elif choice == "3":
        display_capes("All")
      elif choice == "+":
        create_team()
      elif choice == "x":
        break

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    
    display_welcome() #WELCOME PAGE
    start_main_menu()
      




