class PlayerStats:  # pylint: disable=too-few-public-methods
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        nationality_players = [
            player
            for player in self._players
            if player.nationality == nationality
        ]
        return sorted(
            nationality_players, key=lambda player: player.points, reverse=True
        )
