from models import Cape, Team, db


def get_all_teams():
    return db.session.query(Team).all()

def get_team_by_id(id):
    return db.session.get(Team, id)

def get_capes_on_team(team):
    pass