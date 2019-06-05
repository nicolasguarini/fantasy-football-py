import os
from utils import (PlayerNotFoundError,
                   NotEnoughPlayersError,
                   NotEnoughBudgetError,
                   NotCreatedFormationError)

from market import market
from team import Team
from match import Match
from players_registry import players


def clear():
    os.system("clear")


def fill_teams(teams):
    new_team_name = "milan"
    new_team_budget = 350
    new_team = Team(new_team_name, new_team_budget)
    new_team.players = players[:11]
    teams.append(new_team)

    new_team_name = "juventus"
    new_team_budget = 643
    new_team = Team(new_team_name, new_team_budget)
    new_team.players = players[11:22]
    teams.append(new_team)


def menu():
    teams = []
    fill_teams(teams)

    while True:
        clear()
        print("1 - New team\n")
        print("2 - Manage teams\n")
        print("3 - New match\n")
        print("0 - Quit\n")
        user_choice = int(input("Insert your choice: "))

        if user_choice == 1:
            new_team(teams)
        elif user_choice == 2:
            manage_teams(teams)
        elif user_choice == 3:
            new_match(teams)
            pass
        elif user_choice == 0:
            return


def new_team(teams):
    clear()
    new_team_name = input("Insert the name of the team you want to create: ")
    new_team_budget = 1500
    new_team = Team(new_team_name, new_team_budget)
    teams.append(new_team)


def manage_teams(teams):
    clear()
    while True:
        clear()

        for teams_counter in range(0, len(teams)):
            print('%d - %s \n' % (teams_counter+1, teams[teams_counter].name))
        print("0 - Back\n")

        team_index = int(input("Insert the team you want to manage: "))

        if team_index == 0:
            return
        else:
            team_index -= 1

        manage_team(teams, team_index)


def new_match(teams):
    clear()
    cont = 0
    teams_playing = []

    while cont < 2:
        clear()
        for teams_counter in range(0, len(teams)):
            print('%d - %s \n' % (teams_counter+1, teams[teams_counter].name))
        print("0 - Back\n")
        team_index = int(input("Insert the team %s: " % (cont + 1)))

        if team_index == 0:
            return
        else:
            team_index -= 1

        if teams[team_index].formation is None:
            print("The selected team has no valid formation. Please go back to 'Manage teams' and create one!!")
            input("Hit ENTER to continue...")
            continue

        teams_playing.append(teams[team_index])
        cont += 1

    match = Match(teams_playing[0], teams_playing[1])
    clear()
    match.play()
    input("Hit ENTER to continue...")


def manage_team(teams, team_index):
    while True:
        clear()
        print("--- " + teams[team_index].name + " ---\n")
        print("Available budget: " + str(teams[team_index].budget) +"\n")
        print("1 - Buy players\n")
        print("2 - Sell players\n")
        print("3 - Display market\n")
        print("4 - Display team's players\n")
        print("5 - Compose formation\n")
        print("6 - Display formation\n")
        print("0 - Back\n")
        user_choice = int(input("Insert your choice: "))
        
        if user_choice == 1:
            try:
                buy(teams, team_index)
            except PlayerNotFoundError:
                print("Player non found")
                input("Hit ENTER to continue...")

        elif user_choice == 2:
            try:
                sell(teams, team_index)
            except PlayerNotFoundError:
                print("Player non found")
                input("Hit ENTER to continue...")
        
        elif user_choice == 3:
            print_market()
            input("Hit ENTER to continue...")

        elif user_choice == 4:
            clear()
            teams[team_index].print_players()
            input("Hit ENTER to continue...")

        elif user_choice == 5:
            try:
                compose_formation(teams[team_index])
            except NotEnoughPlayersError:
                print("You don't have enough players!!!")
                input("Hit ENTER to continue...")

        elif user_choice == 6:
            clear()
            try:
                teams[team_index].print_formation()
            except NotCreatedFormationError:
                print("Devi prima creare una formation!!")
            input("Hit ENTER to continue")

        elif user_choice == 0:
            return


def compose_formation(team):
    clear()
    minimum_players = 11

    if len(team.players) < minimum_players:
        raise NotEnoughPlayersError
    
    players_temp = team.players.copy()
    summoned = []

    if len(players_temp) == minimum_players:
        summoned = players_temp.copy()
        team.compose_formation(summoned)
        print("Formation composed automatically")
        input("Hit ENTER to continue...")
        return

    cont = 0
    while cont < minimum_players:
        clear()
        print("--\nGiocatore %d\n--\n" % (cont + 1))
        for player in players_temp:
            player.print_player()
        
        surname_player_to_sell = input("Insert the surname of the player: ")
        name_player_to_sell = input("Insert the name of the player: ")
        
        for player in players_temp: 
            if surname_player_to_sell == player.surname:
                if name_player_to_sell == player.name:
                    players_temp.remove(player)
                    summoned.append(player)
                    cont += 1
                    break
    team.compose_formation(summoned)


def buy(teams, team_index):
    clear()
    found = False
    market.print_free_players()

    surname_player_to_buy = input("Insert the surname of the player: ")
    name_player_to_buy = input("Insert the name of the player: ")

    for free_player in market.players: 
        if surname_player_to_buy == free_player.surname:
            if name_player_to_buy == free_player.name:
                try:
                    teams[team_index].buy_player(free_player)
                except NotEnoughBudgetError:
                    print("Not enough budget!")
                    input("Hit ENTER to continue...")
                    return
                market.players.remove(free_player)
                found = True
                break

    if not found:
        raise PlayerNotFoundError


def sell(teams, team_index):
    clear()
    found = False
    if len(teams[team_index].players) == 0:
        print("Buy first some players!!!")
        input("Hit ENTER to continue...")
        return
    
    for player in teams[team_index].players:
        player.print_player()
    
    surname_player_to_sell = input("Insert the surname of the player: ")
    name_player_to_sell = input("Insert the name of the player: ")

    for player in teams[team_index].players: 
        if surname_player_to_sell == player.surname:
            if name_player_to_sell == player.name:
                found = True
                teams[team_index].sell_player(player)
                market.players.append(player)
                break
    
    if not found:
        raise PlayerNotFoundError


def print_market():
    clear()
    print("1 - Display Strikers\n")
    print("2 - Display Defenders\n")
    print("3 - Display Midfielders\n")
    print("4 - Display Goalkeepers\n")
    print("5 - Display All\n")
    user_choice = int(input("Insert your choice"))

    if user_choice == 1:
        strikers = market.strikers()
        for striker in strikers:
            striker.print_player()
    elif user_choice == 2:
        defenders = market.defenders()
        for defender in defenders:
            defender.print_player()
    elif user_choice == 3:
        midfielders = market.midfielders()
        for midfielder in midfielders:
            midfielder.print_player()
    elif user_choice == 4:
        goalkeepers = market.goalkeepers()
        for goalkeeper in goalkeepers:
            goalkeeper.print_player()
    elif user_choice == 5:
        market.print_free_players()


if __name__ == "__main__":
    menu()
