import requests
import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
import webbrowser
from bs4 import BeautifulSoup
from .env import session_id


s = requests.Session()

def input_parser(day: str, t=['double_el', 'intlist']):
    s = requests.Session()
    r = s.get(f"https://adventofcode.com/2021/day/{day}/input",
              cookies={'session': session_id})
    res = r.text.strip().split("\n")
    
    if t == "double_el":
        res = r.text.strip().replace("\n\n", "\n").split("\n")
    elif t == "intlist":
        sp = res[0].split(",")
        res =  list(int(elem) for elem in sp)
        
    return res


def open_exercise_instructions(day):
    webbrowser.open(f"https://adventofcode.com/2021/day/{day}")



def current_stars():
    res = s.get("https://adventofcode.com/2021", cookies={'session': session_id}).text


    soup = BeautifulSoup(res, features="lxml")
    user = list(soup.find_all("div", {"class": "user"})[0].descendants)[0].text
    stars = soup.find_all("span", {"class": "star-count"})[0].text

    return f"{user}: {stars}"


def post_answer(day: str, answer):

    data = {
        "answer": answer
    }

    return s.post(f"https://adventofcode.com/2021/day/{day}/answer",
            cookies={'session': session_id,
            "_ga": "GA1.2.1573411548.1638607812",
            "_gid": "GA1.2.365211044.1638711996"},
            data=answer)
