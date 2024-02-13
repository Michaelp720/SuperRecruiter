from models import Cape, Team, db
from simple_term_menu import TerminalMenu
import sys


sys.settrace

def get_all_teams():
    return db.session.query(Team).all()

def get_team_by_id(id):
    return Team.query.filter(Team.id == id).first()

def get_capes_on_team(id):
    return Cape.query.filter(Cape.team_id == id)    

def get_cape_by_id(id):
    return Cape.query.filter(Cape.id == id).first()

def change_capes_team(cape):
    team_names = [team.team_name for team in get_all_teams()]
    team_names.append("no team")
    title = "Which team will they join?"
    #print(team_names)
    #new_team, index = pick(team_names, title)
    terminal_menu = TerminalMenu(team_names)
    menu_entry_index = terminal_menu.show()
    print(menu_entry_index)
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

def delete_cape(cape):
    print(f"{cape.name} deleted")
    Cape.query.filter(Cape.id == cape.id).delete()
    db.session.commit()