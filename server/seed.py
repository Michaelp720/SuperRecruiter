from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
    new_superheroes = [
            Superhero(
                cape_name = "Fallen Angel",
                classification = "Striker 3, Blaster 2, Mover 5, Thinker 3"
                powers = "pyrokinesis, matter generation, flight, air current perception",
                allignment = "Villain",
                team_id = 
            ),
            Superhero(
                cape_name = "Pulse",
                classification = "Striker 7, Mover 6"
                powers = "bursts of propulsive green light",
                allignment = "Hero",
                team_id = 
            ),
            Superhero(
                cape_name = "Bear",
                classification = "Breaker 5, Striker 6, Mover 2"
                powers = "Breaker form",
                allignment = "Villain",
                team_id = 
            ),
            Superhero(
                cape_name = "Claymore",
                classification = "Striker 5, Mover 4, Blaster 2"
                powers = "Breaker form",
                allignment = "Vigillante",
                team_id = 
            )
        ]

    db.session.add_all(new_superheroes) #add_all to add a list
    db.session.commit()