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

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        team_players = [
            player for player in self._players if player.team == team
        ]
        return sorted(team_players, key=lambda player: player.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä"""
        return sorted(self._players, key=lambda player: player.goals, reverse=True)[:how_many]
