from config import db
#from rich import print

class Cape(db.Model):
    __tablename__ = 'capes'

    id = db.Column(db.Integer, primary_key = True)
    cape_name = db.Column(db.String, unique = True) #other constraints too, unique- no two rows can have same name
    classification = db.Column(db.String)
    powers = db.Column(db.String)
    allignment = db.Column(db.String)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id')) #foreign key links each Cape (row) to a team in a one to many relationship

    def __repr__(self): #changes how a Cape is printed
        return f'{id}: Name: {self.cape_name} Classification: {self.classification} Powers: {self.powers}'

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key = True)
    team_name = db.Column(db.String) 
    allignment = db.Column(db.String)

    def __repr__(self):
        return f'{id} Name: {self.team_name} allignment: {self.allignment}'