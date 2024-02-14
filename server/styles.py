from rich import print
from rich.style import Style
from rich.text import Text
from models import Cape, Team, db
from db_utils import get_cape_status


page_heading_style = Style(color = "#E4C31C", bold = True)

#colors
#Heros and menu titles: E4C31C
#Villains: #872667
#options: green

def cape_panel(cape, is_all):
    id = cape.id
    name = cape.cape_name
    classification = cape.classification
    
    
    if is_all:
        team_id = cape.team_id
        if team_id:
            team_name = Team.query.filter(Team.id == team_id).first().team_name
        else:
            team_name = ""
        allignment = cape.allignment
        cape_status = get_cape_status(allignment, team_name, team_id)
        return f"[bold green]{id}[/]: [bold]{name}[/]\n{classification}\n{cape_status}"
    else:
        return f"[bold green]{id}[/]: [bold]{name}[/]\n{classification}"
