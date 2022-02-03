n, m = [int(e) for e in input().split()]


class Club:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.count_of_players = 0

    def add(self):
        self.count_of_players += 1

    def remove(self):
        self.count_of_players -= 1

    def __hash__(self):
        return hash((self.name, self.city))


class Player:
    def __init__(self, name, club):
        self.name = name
        self.club = club
        self.club.add()

    def leave(self):
        self.club.remove()
        self.club = None

    def change(self, new_club):
        self.club.remove()
        self.club = new_club
        new_club.add()


players = dict()
clubs = dict()
city_to_club = dict()

for _ in range(n):
    name, city, team_players = input().split(" ", 2)
    team_players = set(team_players.split())
    club = Club(name, city)
    if city in city_to_club:
        city_to_club[city].append(club)
    else:
        city_to_club[city] = [club]

    clubs[name] = club
    for player in team_players:
        players[player] = Player(player, club)

for _ in range(m):
    command = input().split()
    if len(command) == 1:
        player_name = command[0]
        players[player_name].leave()
    elif len(command) == 2:
        player_name, to_club = command
        club = clubs[to_club]
        players[player_name] = Player(player_name, club)
    else:
        player_name, from_club, to_club = command
        players[player_name].change(clubs[to_club])
    for club_name in clubs:
        club = clubs[club_name]
        if club.count_of_players < 5:
            club.count_of_players = 0

cities = sorted(city_to_club.keys())
for city in cities:
    playable_teams = 0
    for club in city_to_club[city]:
        if club.count_of_players >= 5:
            playable_teams += 1
    if playable_teams > 0:
        print(city)

