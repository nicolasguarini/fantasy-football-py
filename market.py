from player import Roles
from players_registry import players


class Market:
    def __init__(self): 
        self.players = players

    def strikers(self):
        strikers = []

        for player in self.players:
            if player.role == Roles.striker:
                strikers.append(player)

        return strikers

    def midfielders(self):
        midfielders = []

        for player in self.players:
            if player.role == Roles.midfielder:
                midfielders.append(player)

        return midfielders

    def defenders(self):
        defenders = []

        for player in self.players:
            if player.role == Roles.defender:
                defenders.append(player)

        return defenders

    def goalkeepers(self):
        goalkeepers = []

        for player in self.players:
            if player.role == Roles.goalkeeper:
                goalkeepers.append(player)

        return goalkeepers

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def print_free_players(self):
        for free_player in self.players:
            free_player.print_player()


market = Market()

