from models import Cape, Team, db


def get_all_teams():
    return db.session.query(Team).all()

def get_team_by_id(id):
    # return db.session.get(Team, id)
    return Team.query.filter(Team.id == id).first()

def get_capes_on_team(id):
    return Cape.query.filter(Class.team_id == id)    

def get_cape_by_id(id):
    return Cape.query.filter(Class.id == id) 