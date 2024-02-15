from models import Cape, Team, db
from simple_term_menu import TerminalMenu
import sys 


sys.settrace

def get_all_teams():
    return db.session.query(Team).all()

def get_team_by_id(id):
    return Team.query.filter(Team.id == id).first()

def get_capes_on_team(id):
    if id == "All" or id == "game":
        return Cape.query.all()
    else:
        return Cape.query.filter(Cape.team_id == id)    

def get_cape_by_id(id):
    return Cape.query.filter(Cape.id == id).first()

def change_capes_team(cape):
    team_names = [team.team_name for team in get_all_teams()]
    team_names.append("no team")
    terminal_menu = TerminalMenu(team_names)
    menu_entry_index = terminal_menu.show()
    new_team = team_names[menu_entry_index]
    if new_team != "no team":
        team_obj = Team.query.filter(Team.team_name == new_team).first()
        cape.team_id = team_obj.id
        cape.allignment = team_obj.allignment
        print(f"{cape.cape_name} has joined the {cape.allignment} {team_names[menu_entry_index]}!")
    else:
        cape.team_id = None
        print(f"{cape.cape_name} has gone solo")
    db.session.commit()
    return cape.team_id

def delete_cape(cape):
    print(f"{cape.cape_name} deleted")
    Cape.query.filter(Cape.id == cape.id).delete()
    db.session.commit()

def create_cape(team_id):
    name_input = input("Cape name: ")
    powers_input = input(f"Describe {name_input}'s powers: ")
    print("Learn more about Parahumans power classifications: https://worm.fandom.com/wiki/Power_Classifications")
    classification_input = input("Classifications: ") #add terminal menu to choose classifications?

    if not team_id:
        print(f"How does {name_input} allign?")
        allignment_options = ["Heroic", "Villainous"]
        terminal_menu = TerminalMenu(allignment_options)
        menu_entry_index = terminal_menu.show()
        allignment_input = allignment_options[menu_entry_index]
    elif team_id == "All":
        allignment_input = None
    else:
        allignment_input = Team.query.filter(Team.id == team_id).first().allignment

    new_cape = Cape(
        cape_name = name_input,
        classification = classification_input,
        powers = powers_input,
        allignment = allignment_input,
        team_id = team_id
    )

    if team_id == "All":
        team_id = change_capes_team(new_cape)

    db.session.add(new_cape)
    db.session.commit()
    if team_id:
        print(f"{name_input} has joined {Team.query.filter(Team.id == team_id).first().team_name}")
    else:
        print(f"{name_input} has been created")
    return team_id

def create_team():
    name_input = input("What will your team be named? ")
    print(f"How does {name_input} allign?")
    allignment_options = ["Heroic", "Villainous"]
    terminal_menu = TerminalMenu(allignment_options)
    menu_entry_index = terminal_menu.show()
    allignment_input = allignment_options[menu_entry_index]

    team = Team(
        team_name = name_input,
        allignment = allignment_input
    )

    db.session.add(team)
    db.session.commit()
    print(f"{name_input} has been created") #placeholder, will become recruiting game
    return Team.query.filter(Team.team_name == name_input)


def get_cape_status(allignment, team_name, team_id):
    if allignment == "Heroic":
        if team_id:
            cape_status = f"[#A1B8CE]Hero with[/] [#E4C31C]{team_name}[/]"
        else:
            cape_status = f"[#A1B8CE]Vigilante[/]"
    elif allignment == "Villainous":
        if team_id:
            cape_status = f"[#A1B8CE]Villain with[/] [#872667]{team_name}[/]"
        else:
            cape_status = f"[#A1B8CE]Solo Villain[/]"

    return cape_status

def handle_recruiting(cape, my_team):
    cape.team_id = my_team.id
    cape.allignment = my_team.allignment
    db.session.commit()
