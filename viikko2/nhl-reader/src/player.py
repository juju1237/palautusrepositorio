class Player:
    def __init__(self, player_data):
        self.name = player_data["name"]
        self.nationality = player_data["nationality"]
        self.team = player_data["team"]
        self.goals = player_data["goals"]
        self.assists = player_data["assists"]

    def __str__(self):
        return (
            f"{self.name} team {self.team}  "
            f"goals {self.goals} assists {self.assists}"
        )
