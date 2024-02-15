from config import db
import json
#from rich import print

class Cape(db.Model):
    __tablename__ = 'capes'

    id = db.Column(db.Integer, primary_key = True)
    cape_name = db.Column(db.String, unique = True) #other constraints too, unique- no two rows can have same name
    classification_json = db.Column(db.Text)
    powers = db.Column(db.String)
    allignment = db.Column(db.String)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id')) #foreign key links each Cape (row) to a team in a one to many relationship

    def __init__(self, cape_name, classification, powers, allignment, team_id):
        self.cape_name = cape_name
        self.classification_json = json.dumps(classification)
        self.powers = powers
        self.allignment = allignment
        self.team_id = team_id


    @property
    def classification(self):
        return json.loads(self.classification_json)


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key = True)
    team_name = db.Column(db.String) 
    allignment = db.Column(db.String)

    def __repr__(self):
        return f'{self.id}: Name: {self.team_name} allignment: {self.allignment}'

class ActionEffect(db.Model):
    __tablename__ = 'action_effects'

    id = db.Column(db.Integer, primary_key = True)
    quality_name = db.Column(db.String, unique = True)
    ambush = db.Column(db.Integer) 
    outwit = db.Column(db.Integer)
    overpower = db.Column(db.Integer)
    convince = db.Column(db.Integer)
    extort = db.Column(db.Integer)
    bribe = db.Column(db.Integer)
