import csv
import networkx as nx


class Game:
    def __init__(self, matchday, id, home, away, score_home, score_away):
        self.matchday = int(matchday)
        self.id = id
        self.home = home
        self.away = away
        self.score_home = score_home
        self.score_away = score_away
        
    def __str__(self):
        return f"{self.home} vs. {self.away} {self.score_home}:{self.score_away}"
        
    def isDraw(self):
        return self.score_home == self.score_away
    
    def winner(self):
        if self.score_home > self.score_away:
            return self.home
        elif self.score_away > self.score_home:
            return self.away
        else:
            return "DRAW"


def read_games(filename = '08_winningPossibilities_hbl1718.csv'):
    
    games = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            games.append(Game(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return games


games = read_games()


def teams():
    teams = set()

    for game in games:
        if game.home not in teams:
            teams.add(game.home)
    
    return teams


teams = teams()


def get_current_points(matchday):
    points = dict([(team, 0) for team in teams])
    for game in games:
        if game.matchday <= matchday:
            if game.isDraw():
                points[game.home] = points[game.home] + 1
                points[game.away] += 1
            else:
                points[game.winner()] += 2

    return points


def get_remaining_games_graph(matchday):
    
    g = nx.MultiGraph()
    g.add_nodes_from(teams)
    
    for game in games:
        if game.matchday > matchday:
            g.add_edge(game.home, game.away)
    
    return g


def print_table(matchday):
    # get points after matchday
    points = get_current_points(matchday)
    
    # sort teams by points
    table = sorted(points.items(), key=lambda kv: -kv[1])
    
    # column widths for printing table
    col1_len = 4
    col2_len = max([len(t[0]) for t in table])
    col3_len = 6
    
    # print table
    print(f"Table after matchday {matchday}:")
    print("+-" + "-" * col1_len + "-+-" + "-" * col2_len + "-+-" + "-" * col3_len + "-+")
    print(f"| Rank | {'Team':<{col2_len}} | Points |")
    print("+-" + "-" * col1_len + "-+-" + "-" * col2_len + "-+-" + "-" * col3_len + "-+")
    for i in range(len(table)):
        print(f"| {i+1:>{col1_len}} | {table[i][0]:<{col2_len}} | {table[i][1]:>{col3_len}} |")
    print("+-" + "-" * col1_len + "-+-" + "-" * col2_len + "-+-" + "-" * col3_len + "-+")
