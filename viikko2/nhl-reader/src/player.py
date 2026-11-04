class Player:
    def __init__(self, player_data):
        self.name = player_data["name"]
        self.nationality = player_data["nationality"]
        self.team = player_data["team"]
        self.goals = player_data["goals"]
        self.assists = player_data["assists"]

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return (
            f"{self.name:22} {self.team:15} "
            f"{self.goals:2} + {self.assists:2} = {self.points}"
        )
