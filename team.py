from utils import NotEnoughBudgetError
from utils import NotCreatedFormationError


class Team:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.players = []
        self.formation = None

    def compose_formation(self, summoned):
        self.formation = Formation(players=summoned)

    def buy_player(self, player):
        if player.price > self.budget:
            raise NotEnoughBudgetError
        self.players.append(player)
        self.budget -= player.price

    def sell_player(self, player):
        self.players.remove(player)
        self.budget += player.price

    def print_players(self):
        for player in self.players:
            player.print_player()

    def print_formation(self):
        if self.formation is None:
            raise NotCreatedFormationError
            
        for player in self.formation.players:
            player.print_player()


class Formation:
    def __init__(self, players):
        self.players = players

    def strength(self):
        strength_sum = 0

        for player in self.players:
            strength_sum += player.strength
        medium_strength = strength_sum / len(self.players)

        return medium_strength
