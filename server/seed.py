from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():

    Cape.query.delete()
    Team.query.delete()
    ActionEffect.query.delete()
    print("all db data deleted")

    new_teams = [
      Team(
          team_name = "Team Sunburst",
          allignment = "Heroic"
      ),
      Team(
          team_name = "Sonic Alliance",
          allignment = "Heroic"
      ),
      Team(
          team_name = "Shadow Syndicate",
          allignment = "Villainous"
      ),
      Team(
          team_name = "Cyclone Cartel",
          allignment = "Villainous"
      )
    ]

    db.session.add_all(new_teams) #add_all to add a list
    db.session.commit()

    new_capes = [
        Cape(
            cape_name = "Fallen Angel",
            classification = {"Striker": 3, "Blaster": 2, "Mover": 5, "Thinker": 3},
            powers = "pyrokinesis, matter generation, flight, air current perception",
            allignment = "Heroic",
            team_id = None
        ),
        Cape(
            cape_name = "Pulse",
            classification = {"Striker": 7, "Mover": 6},
            powers = "generates bursts of propulsive green light",
            allignment = "Heroic",
            team_id = None
        ),
        Cape(
            cape_name = "Typhon",
            classification = {"Breaker": 5, "Brute": 6, "Mover": 2, "Thinker": 1},
            powers = "Bear-avatar form, size changing, invulnerability",
            allignment = "Villainous",
            team_id = None
        ),
        Cape(
            cape_name = "Claymore",
            classification = {"Striker": 5, "Mover": 4, "Blaster": 2},
            powers = "Gravity/mass manipulation of self and sword",
            allignment = "Heroic",
            team_id = None
        ),
        Cape(
            cape_name = "Mechimera",
            classification = {"Tinker": 8, "Trump": 8},
            powers = "Creates short-lived technology and power-suits to mimic or neutralize powers",
            allignment = "Villainous",
            team_id = None
        ),
        Cape(
            cape_name = "Capsule",
            classification = {"Shaker": 4},
            powers = "Creates pocket dimensions where time runs at different rates",
            allignment = "Villainous",
            team_id = None
        ),
        Cape(
            cape_name = "Solar Flare",
            classification = {"Blaster": 8, "Mover": 7},
            powers = "Harnesses solar energy for devastating energy blasts, flight at incredible speeds",
            allignment = "Heroic",
            team_id = Team.query.filter(Team.team_name == "Team Sunburst").first().id
        ),
        Cape(
            cape_name = "Specter",
            classification = {"Master": 5, "Thinker": 6},
            powers = "Can manipulate shadows to create illusions and confuse enemies, heightened perception and tactical analysis",
            allignment = "Heroic",
            team_id = Team.query.filter(Team.team_name == "Team Sunburst").first().id
        ),
        Cape(
            cape_name = "Tempest",
            classification = {"Blaster": 6, "Shaker": 4, "Mover": 5},
            powers = "Controls weather patterns, creates storms and lightning, can ride wind currents at high speeds",
            allignment = "Heroic",
            team_id = Team.query.filter(Team.team_name == "Team Sunburst").first().id
        ),
        Cape(
            cape_name = "Echo",
            classification = {"Striker": 4, "Thinker": 7},
            powers = "Can replicate and amplify sounds, heightened auditory perception for tracking and analysis",
            allignment = "Heroic",
            team_id = Team.query.filter(Team.team_name == "Sonic Alliance").first().id
        ),
        Cape(
            cape_name = "Morphic",
            classification = {"Changer": 9, "Brute": 4, "Mover": 6},
            powers = "Shape-shifting abilities, enhanced strength and durability, can move swiftly by altering form",
            allignment = "Heroic",
            team_id = Team.query.filter(Team.team_name == "Sonic Alliance").first().id
        ),
        Cape(
            cape_name = "Nebula",
            classification = {"Blaster": 7, "Striker": 5},
            powers = "Manipulates cosmic energy to create blasts and energy constructs, can teleport short distances",
            allignment = "Heroic",
            team_id = Team.query.filter(Team.team_name == "Sonic Alliance").first().id
        ),
        Cape(
            cape_name = "Darkfire",
            classification = {"Blaster": 9, "Shaker": 6},
            powers = "Controls dark flames that consume everything they touch, creates dark energy fields to trap enemies",
            allignment = "Villainous",
            team_id = Team.query.filter(Team.team_name == "Shadow Syndicate").first().id
        ),
        Cape(
            cape_name = "Nightshade",
            classification = {"Master": 6, "Stranger": 8},
            powers = "Summons shadowy minions from other dimensions, can blend into shadows and become nearly invisible",
            allignment = "Villainous",
            team_id = Team.query.filter(Team.team_name == "Shadow Syndicate").first().id
        ),
        Cape(
            cape_name = "Ragnarok",
            classification = {"Brute": 10, "Breaker": 7},
            powers = "Transforms into an unstoppable juggernaut of destruction, wrecks havoc with seismic shockwaves",
            allignment = "Villainous",
            team_id = Team.query.filter(Team.team_name == "Shadow Syndicate").first().id
        ),
        Cape(
            cape_name = "Vortex",
            classification = {"Mover": 8, "Striker": 7},
            powers = "Creates whirlwinds and tornadoes to devastate areas, can deliver devastating blows with wind-enhanced strikes",
            allignment = "Villainous",
            team_id = Team.query.filter(Team.team_name == "Cyclone Cartel").first().id
        ),
        Cape(
            cape_name = "Blackout",
            classification = {"Shaker": 7, "Blaster": 6},
            powers = "Generates dark energy fields to block out light and sound, shoots bolts of darkness that drain energy",
            allignment = "Villainous",
            team_id = Team.query.filter(Team.team_name == "Cyclone Cartel").first().id
        ),
        Cape(
            cape_name = "Shadowstrike",
            classification = {"Striker": 7, "Mover": 6},
            powers = "Moves swiftly between shadows, delivers powerful melee strikes enhanced by darkness",
            allignment = "Heroic",
            team_id = None
        ),
        Cape(
            cape_name = "Blade Runner",
            classification = {"Striker": 8, "Thinker": 5},
            powers = "Master of edged weapons, possesses enhanced reflexes and tactical awareness in combat",
            allignment = "Heroic",
            team_id = None
        ),
        Cape(
            cape_name = "Vigil",
            classification = {"Breaker": 6, "Thinker": 7},
            powers = "Transforms into an incorporeal shadow form, gains heightened senses and intuition",
            allignment = "Heroic",
            team_id = None
        ),
        Cape(
            cape_name = "Nemesis",
            classification = {"Master": 9, "Trump": 4},
            powers = "Creates duplicates of themselves with independent thought and action, each possessing a fraction of the original's power",
            allignment = "Villainous",
            team_id = None
        ),
        Cape(
            cape_name = "Eclipse",
            classification = {"Shaker": 8, "Stranger": 6},
            powers = "Manipulates shadows and darkness on a large scale, can obscure and distort perceptions",
            allignment = "Villainous",
            team_id = None
        ),
        Cape(
            cape_name = "Rogue",
            classification = {"Striker": 6, "Thinker": 8},
            powers = "Absorbs and temporarily mimics the powers of other parahumans on touch, gains insights into their abilities and weaknesses",
            allignment = "Villainous",
            team_id = None
        )
    ]

    db.session.add_all(new_capes) #add_all to add a list
    db.session.commit()


    qualities = [
      ActionEffect(
        quality_name = "on_team",
        ambush = 12,
        outwit = 0,
        overpower = 5,
        convince = 0,
        extort = -5,
        bribe = 3   
      ),
      ActionEffect(
        quality_name = "solo",
        ambush = -3,
        outwit = 0,
        overpower = -3,
        convince = -5,
        extort = 0,
        bribe = -5   
      ),
      ActionEffect(
        quality_name = "Heroic",
        ambush = 0,
        outwit = 0,
        overpower = 0,
        convince = -3,
        extort = -5,
        bribe = 5   
      ),
      ActionEffect(
        quality_name = "Villainous",
        ambush = 1,
        outwit = 0,
        overpower = 0,
        convince = -3,
        extort = 3,
        bribe = -3   
      ),
      ActionEffect(
        quality_name = "Thinker",
        ambush = 5,
        outwit = 5,
        overpower = -3,
        convince = 3,
        extort = 5,
        bribe = -3   
      ),
      ActionEffect(
        quality_name = "Stranger",
        ambush = 10,
        outwit = 0,
        overpower = -5,
        convince = 0,
        extort = 5,
        bribe = 0   
      ),
      ActionEffect(
        quality_name = "Tinker",
        ambush = -5,
        outwit = 5,
        overpower = 0,
        convince = 0,
        extort = 0,
        bribe = -5   
      ),
      ActionEffect(
        quality_name = "Master",
        ambush = 5,
        outwit = 0,
        overpower = -3,
        convince = 5,
        extort = 0,
        bribe = 3   
      ),
      ActionEffect(
        quality_name = "Brute",
        ambush = 3,
        outwit = -5,
        overpower = 10,
        convince = -2,
        extort = -2,
        bribe = -2   
      ),
      ActionEffect(
        quality_name = "Shaker",
        ambush = -5,
        outwit = 0,
        overpower = 2,
        convince = 0,
        extort = 0,
        bribe = 0   
      ),
      ActionEffect(
        quality_name = "Mover",
        ambush = 0,
        outwit = 0,
        overpower = -5,
        convince = 0,
        extort = 0,
        bribe = 0   
      ),
      ActionEffect(
        quality_name = "Breaker",
        ambush = -5,
        outwit = -5,
        overpower = 3,
        convince = 0,
        extort = 0,
        bribe = 0   
      ),
      ActionEffect(
        quality_name = "Blaster",
        ambush = -3,
        outwit = 0,
        overpower = 1,
        convince = 0,
        extort = 0,
        bribe = 0   
      ),
      ActionEffect(
        quality_name = "Striker",
        ambush = -3,
        outwit = 0,
        overpower = 3,
        convince = 0,
        extort = 0,
        bribe = 0   
      ),
      ActionEffect(
        quality_name = "Changer",
        ambush = -5,
        outwit = -5,
        overpower = 0,
        convince = 0,
        extort = 0,
        bribe = 0   
      ),
      ActionEffect(
        quality_name = "Trump",
        ambush = -3,
        outwit = -3,
        overpower = 10,
        convince = 0,
        extort = 0,
        bribe = 0   
      )
    ]

    db.session.add_all(qualities)
    db.session.commit()
    print("db seeded")