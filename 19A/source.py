class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.points = 0
        self.dif = 0
        self.score = 0

    def get_result(self, scr, allowed):
        self.score += scr
        self.dif += scr - allowed
        if scr > allowed:
            self.points += 3
        elif scr == allowed:
            self.points += 1

    def display(self):
        print(f'{self.team_name}\t{self.points}\t{self.dif}\t{self.score}')

    def comp(self, team2):
        if self.points < team2.points:
            return True
        elif self.points == team2.points and self.dif < team2.dif:
            return True
        elif self.points == team2.points and self.dif == team2.dif and self.score < team2.score:
            return True
        else:
            return False


result = {}
list_team = []
n = int(input())
for i in range(n):
    name = input()
    t = Team(name)
    list_team.append(t)

num_of_matches = n*(n-1)//2
for match in range(num_of_matches):
    inp = input()
    versus = inp.split()
    result[versus[0]] = versus[1]

start = 0
for order, game in result.items():
    vs = order.split("-")
    res = game.split(":")
    for t1 in range(len(list_team)):
        if list_team[t1].team_name == vs[0]:
            list_team[t1].get_result(int(res[0]), int(res[1]))
        if list_team[t1].team_name == vs[1]:
            list_team[t1].get_result(int(res[1]), int(res[0]))

for i in range(len(list_team) - 1):
    for j in range(i + 1, len(list_team)):
        if list_team[i].comp(list_team[j]):
            list_team[i], list_team[j] = list_team[j], list_team[i]

tname = []
for i in range(len(list_team)//2):
    tname.append(list_team[i].team_name)

tname = sorted(tname)
for i in range(len(tname)):
    print(tname[i])