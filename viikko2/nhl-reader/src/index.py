import requests
from player import Player


def print_players_by_nationality(players, nationality):
    print(f"Players from {nationality}\n")
    nationality_players = [
        player for player in players if player.nationality == nationality
    ]
    for player in sorted(
        nationality_players, key=lambda player: player.points, reverse=True
    ):
        print(player)


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = [Player(player_data) for player_data in response]

    print_players_by_nationality(players, "FIN")


if __name__ == "__main__":
    main()
