import datetime as dt

class Game:
  def __init__(self, home_team, visiting_team, home_score, visitor_score, other):
    self.home_team = home_team
    self.visiting_team = visiting_team
    self.home_score = home_score
    self.visitor_score = visitor_score
    self.home_diff = self.home_score - self.visitor_score
    self.neutral_site = (other.strip() != "")
    self.date = ""
  def setDate(s): 
    """accepts a string in mm/dd/yyyy format
       converts to date
    """
    sds = [int(i) for i in s.split("/")]
    self.date = dt.date(sds[2], sds[0], sds[1])

class Team:
  def __init__(self, team_name):
    self.team_name = team_name
    self.team_id = 0

class League:
  def __init__(self):
    self.teams = {}
    self.next_key = 1
  def add_team(self, team):
    if (team.team_name not in self.teams.keys()):
      team_id = self.next_key
      team.team_id = team_id
      self.teams[team.team_name] = team
      self.next_key += 1

ch = "\t"      
def to_str(s):
  return str(s) + ch

#def to_str(s, b): # b can be either -1, 0, or 1 for "before", "both", and "after"
#    st = ""
#    if (b <= 0):
#      st += ch
#    st += str(s)
#    if (b >= 0):
#      st += ch
#    return st

  
class Schedule:
  def __init__(self, league):
    self.games = []
    self.league = league
  def add_game(self, game):
    self.games.append(game)
  def __str__(self):
    s = ""
    for game in self.games:
      s += to_str(game.home_diff)
      home = game.home_team.team_id
      visitor = game.visiting_team.team_id
      not_neutral = 1
      if (game.neutral_site):
        not_neutral = 0
      s += to_str(not_neutral)
      for team in range(len(self.league.teams)):
        col = team + 1
        if (col == home):
          s += to_str(1)
        elif (col == visitor):
          s += to_str(-1)
        else:
          s += to_str(0)
      s = s[0:len(s)-1]
      s += "\n"
    return s


def simple_test():
  l =  League()
  l.add_team(Team("Babcock"))
  l.add_team(Team("Kentucky"))
  l.add_team(Team("Russia"))
  l.add_team(Team("500"))
  s = Schedule(l)
  j = Game(l.teams["Babcock"], l.teams["Kentucky"], 40, 23, "")
  s.add_game(j)
  s.add_game(Game(l.teams["Russia"], l.teams["Babcock"], 24, 30, ""))
  s.add_game(Game(l.teams["500"], l.teams["Russia"], 7, 0, " @ asdf"))
  print s

simple_test()
