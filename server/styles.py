from rich import print
from rich.style import Style
from rich.text import Text
from models import Cape, Team, db
from db_utils import get_cape_status
import time
from rich.console import Console

console = Console()

page_heading_style = Style(color = "#E4C31C", bold = True)
villainous_page_heading_style = Style(color = "#872667", bold = True)


#colors
#Heros and menu titles: #E4C31C
#Villains: #872667
#my team/game: #EB9F25
#options: green
#background/kinda grey: #A1B8CE

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

def team_panel(team):
    id = team.id
    allignment = team.allignment
    team_name = f"[bold]{team.team_name}[/]"
    if allignment == "Heroic":
        allignment_display = f"[#E4C31C]Heroic[/]"
    elif allignment == "Villainous":
        allignment_display = f"[#872667]Villainous[/]"

    return f"[bold green]{id}[/]: {team_name}\n{allignment_display}"

recruiting_style = Style(color = "#EB9F25", bold = True)

def print_recruit_success(text, my_team_name):
    delay = 0.05
    for char in text:
        print(char, end='')
        time.sleep(delay) 
    console.print(f"{my_team_name}", style = recruiting_style)
    time.sleep(2)

# print(f"{target_cape.cape_name} was persuaded! Swayed by {persuasion_adj} they agree to join [bold #EB9F25]{my_team.team_name}[/]")

def print_attempting_recruit(action_type, target_cape_name):
    delay = 0.05
    if action_type == "defeat":
        msg = f"attempting to defeat {target_cape_name}....."
    elif action_type == "persuade":
        msg = f"attempting to persuade {target_cape_name}....."
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(delay)
    time.sleep(1)     
    print("")

def print_recruit_failure(color, msg):
    delay = 0.05
    failure_style = Style(color = color, bold = True)
    for char in msg:
        console.print(char, end='', style = failure_style)
        time.sleep(delay) 
    time.sleep(2)
    