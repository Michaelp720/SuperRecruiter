from db_utils import get_all_teams, get_team_by_id, get_capes_on_team, get_cape_by_id, delete_cape, change_capes_team, create_cape, create_team, get_cape_status, handle_recruiting
from config import app, migrate
from models import Cape, Team, db
from rich import print
from rich.text import Text
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from recruitment import recruitment_success
from simple_term_menu import TerminalMenu

from styles import page_heading_style, cape_panel, team_panel

# Tasks:
# 1. add slow print and pause before success/failure
# 1. change create cape to work with new classification
# 2. error routing and handling

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
  print("[bold green]+[/]: Create new team (start [bold #EB9F25]recruiting game![/])") #will become recruiting game
  print("[bold green]x[/]: Exit")

def get_main_choice():
  return input("What would you like to do? ")

def display_all_teams(): #all teams page
  teams = get_all_teams()
  
  team_renders = [Panel(team_panel(team)) for team in teams]
  console.print(Columns(team_renders))
  choice = get_team_choice()
  display_capes(choice, Team.query.filter(Team.id == choice).first())


def get_team_choice():
  return input("Which team would you like to see? ")

def display_capes(id, my_team): #team details page/solo capes ###############
  print("")
  if not id:
    displayed_team = "solo capes"
    is_all = False
    print("[bold]Solo Capes[/]")
  elif id == "All":
    displayed_team = "all capes"
    is_all = True
    print("[bold]All Capes[/]")
  elif id == "game":
    displayed_team = "game"
    is_all = True
  else:
    displayed_team = display_team(id)
    is_all = False
    
  capes_on_team = get_capes_on_team(id)

  cape_renders = [Panel(cape_panel(cape, is_all)) for cape in capes_on_team]
  console.print(Columns(cape_renders))

  if not my_team:
    print("[bold green]Cape ID[/]: Show cape details")
    print(f"[bold green]+[/]: create a cape to join {displayed_team}")
    print("[bold green]x[/]: return to main menu")
    print("[bold green]other[/]: quit app") #bug? or feature ;)
    choice = get_cape_choice()
    if choice == "+":
      display_capes(create_cape(id), None)
    elif choice == "x":
      start_main_menu()
    else:
      display_cape_details(choice, displayed_team, id)
  elif id != "game":
    print("[bold green]Cape ID[/]: Show cape details")
    print(f"[bold green]+[/]: create a cape to join {displayed_team}")
    print(f"[bold green]r[/]: resume [bold #EB9F25]recruiting game[/] as {displayed_team}")
    print("[bold green]x[/]: return to main menu")
    print("[bold green]other[/]: quit app") #bug? or feature ;)
    choice = get_cape_choice()
    if choice == "+":
      display_capes(create_cape(id), None)
    elif choice == "r":
      display_capes("game", my_team)
    elif choice == "x":
      start_main_menu()
    else:
      display_cape_details(choice, displayed_team, id)
  else:
    print("[bold green]Cape ID[/]: Attempt to [bold #EB9F25]recruit[/] this cape!")
    print("[bold green]x[/]: return to main menu")
    print("[bold green]other[/]: quit app")
    choice = get_cape_choice()
    if choice == "x":
      start_main_menu()
    else:
      attempt_recruitment(Cape.query.filter(Cape.id == choice).first(), my_team)

def get_cape_choice():
  return input("Selection: ")

def display_team(id): #header for team details page
  team = get_team_by_id(id)
  if team.allignment == "Heroic":
    console.print(f'{team.team_name}', style = page_heading_style)
  else:
    console.print(f'{team.team_name}', style = villainous_page_heading_style)
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
    display_capes(team_id, None)
  elif choice == "2":
    change_capes_team(cape)
  elif choice == "-":
    delete_cape(cape)
  else:
    start_main_menu()

def get_cape_dets_choice():
  return input("Selection: ")

def start_game():
  my_team_query = create_team()
  my_team = my_team_query.first()
  display_game_menu(my_team)

  
def display_game_menu(my_team):
  print(f"Recruiting for [bold #EB9F25]{my_team.team_name}[/]")
  print("[bold green]+[/]: attempt to recruit")
  print("[bold green]other[/]: Return to main menu")
  choice = get_game_choice()
  if choice == "+":
    display_capes("game", my_team)


def get_game_choice():
  return input("What would you like to do? ")

def attempt_recruitment(target_cape, my_team):
  console.print(Panel(cape_panel(target_cape, True)))
  print(f"How will you try to recruit {target_cape.cape_name}?")
  action_choice = get_action_choice()
  success = recruitment_success(target_cape, action_choice())

  if success:
    if action_choice == "ambush" or action_choice == "outwit" or action_choice == "overpower":
      if target_cape.allignment == "Heroic":
        allignment_adj = "Impressed"
      elif target_cape.allignment == "Villainous":
        allignment_adj = "Cowed"
      if action_choice == "ambush":
        adjective = "cunning,"
      elif action_choice == "outwit":
        adjective = "strategy,"
      elif action_choice == "overpower":
        adjective = "strength,"
      print(f"{target_cape.cape_name} was defeated! {allignment_adj} by your {adjective} they agree to join [bold #EB9F25]{my_team.team_name}[/]")
    else:
      if action_choice == "convince":
        persuasion_adj = "your pitch,"
      elif action_choice == "extort":
        if target_cape.allignment == "Heroic":
          persuasion_adj = "their guilt,"
        elif target_cape.allignment == "Villainous":
          persuasion_adj = "the threat of embarassment,"
      elif action_choice == "bribe":
        persuasion_adj = "their greed,"
      print(f"{target_cape.cape_name} was persuaded! Swayed by {persuasion_adj} they agree to join [bold #EB9F25]{my_team.team_name}[/]")
    handle_recruiting(target_cape, my_team)
    
  else:
    if action_choice == "ambush" or "outwit" or "overpower":
      if target_cape.allignment == "Heroic":
        failure_msg = "have you sent to the Birdcage."
        color = "#E4C31C"
      elif target_cape.allignment == "Villainous": 
        failure_msg = "end you right here."
        color = "#872667"
      print(f"[#A1B8CE]{target_cape.cape_name}[/]: [bold {color}]'You're lucky I don't {failure_msg}'[/]")
    else:
      if target_cape.allignment == "Heroic":
        allignment_msg = "won't work!"
        villain_flair = ""
        color = "#E4C31C"
      elif target_cape.allignment == "Villainous":
        villain_flair = "pathetic "
        allignment_msg = "is laughable"
        color = "#872667"
      if action_choice == "convince":
        action_msg = "persuade me"
      elif action_choice == "extort":
        action_msg = "pressure me"
      elif action_choice == "bribe":
        action_msg = "buy me off"
      print(f"[#A1B8CE]{target_cape.cape_name}[/]: [bold {color}]'Your {villain_flair}attempt to {action_msg} {allignment_msg}'[/]")
  print("")
  display_game_menu(my_team)

def get_action_choice():
  action_options = ("ambush", "outwit", "overpower", "convince", "extort", "bribe")
  terminal_menu = TerminalMenu(action_options)
  menu_entry_index = terminal_menu.show()
  return action_options[menu_entry_index]

def start_main_menu():
  while True:
      display_main_menu() #MAIN PAGE
      choice = get_main_choice()
      if choice == "1":
        display_all_teams()
      elif choice == "2":
        display_capes(None, None)
      elif choice == "3":
        display_capes("All", None)
      elif choice == "+":
        start_game()
      elif choice == "x":
        break

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    
    display_welcome() #WELCOME PAGE
    start_main_menu()
      




