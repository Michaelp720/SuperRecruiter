from models import Cape, Team, db
from pick import pick
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
    new_team, index = pick(team_names, title)
    if new_team != "no team":
        cape.team_id = Team.query.filter(team_name == new_team).first().id
    else:
        cape.team_id = None
    db.session.commit()

def delete_cape(cape):
    print(f"{cape.name} deleted")
    Cape.query.filter(Cape.id == cape.id).delete()
    db.session.commit()