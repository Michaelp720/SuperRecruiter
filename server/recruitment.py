#recruitment game functions

from models import Cape, ActionEffect, db
from config import app, migrate
from random import randint

actions = ("ambush", "outwit", "overpower", "convince", "extort", "bribe")

def get_difficulty(cape, action):
    classifications = cape.classification

    allignment = cape.allignment
    if cape.team_id:
        on_team = True
    else:
        on_team = False
    
    if len(classifications) >2:
        versatility = 3 + 2*(len(classifications)-3)
    else:
        versatility = 0
    
    # print (f"versatility: {versatility} => 5 expected")

    strengths = {}
    for c in classifications:
        if classifications[c] > 2:
            strengths[c] = classifications[c]
    
    strengths_total_rating = 0
    for c in strengths:
        strengths_total_rating += strengths[c]
    
    # print (f"number of strengths: {len(strengths)} => 2 expected")
    # print (strengths)

    base_difficulty = strengths_total_rating/len(strengths) + versatility
    #10.5

    adjustment = 0
    for c in strengths:
        adjustment += getattr(ActionEffect.query.filter(ActionEffect.quality_name == c).first(), action)
        #print(f"adjustment for {action}, {c}: {getattr(ActionEffect.query.filter(ActionEffect.quality_name == c).first(), action)}")

    if allignment == "Heroic":
        adjustment += getattr(ActionEffect.query.filter(ActionEffect.quality_name == "Heroic").first(), action)
    elif allignment == "Villainous":
        adjustment += getattr(ActionEffect.query.filter(ActionEffect.quality_name == "Villainous").first(), action)
    
    if on_team:
        adjustment += getattr(ActionEffect.query.filter(ActionEffect.quality_name == "on_team").first(), action)
    else:
        adjustment += getattr(ActionEffect.query.filter(ActionEffect.quality_name == "solo").first(), action)

    adjusted_difficulty = base_difficulty + adjustment
    return adjusted_difficulty


    
# if __name__ == "__main__":
#   with app.app_context():
    

    
#     print(get_difficulty(Cape.query.filter(Cape.cape_name == "Typhon").first(), "ambush"))
#     print("6.5 expected")

def recruitment_success(cape, action):
    difficulty = get_difficulty(cape, action)
    print(difficulty)
    roll = randint(1, 20) #balancing? dnd is probaly balanced
    if roll == 1:
        return False
    if roll > difficulty or roll == 20:
        return True
    else:
        return False