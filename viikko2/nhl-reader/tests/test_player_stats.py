"""Yksikkötestit PlayerStats-luokalle."""

import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:  # pylint: disable=too-few-public-methods
    """Palauttaa testipelaajat ilman verkkoyhteyttä."""

    def __init__(self, players):
        self._players = players

    def get_players(self):
        """Palauttaa stubiin tallennetut pelaajat."""
        return self._players


class PlayerStatsTest(unittest.TestCase):
    """Testaa pelaajatilastojen suodatusta ja järjestämistä."""

    def setUp(self):
        self.players = [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "team": "AAA",
                "goals": 20,
                "assists": 30,
            }),
            Player({
                "name": "Player Two",
                "nationality": "FIN",
                "team": "BBB",
                "goals": 25,
                "assists": 15,
            }),
            Player({
                "name": "Player Three",
                "nationality": "SWE",
                "team": "AAA",
                "goals": 10,
                "assists": 35,
            }),
        ]
        self.stats = PlayerStats(PlayerReaderStub(self.players))

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        """Palauttaa vain kansallisuuteen kuuluvat pelaajat pistejärjestyksessä."""
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in result],
            ["Player One", "Player Two"],
        )

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        """Palauttaa vain joukkueeseen kuuluvat pelaajat pistejärjestyksessä."""
        result = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(
            [player.name for player in result],
            ["Player One", "Player Three"],
        )

    def test_top_goal_scorers_returns_requested_number_in_goal_order(self):
        """Palauttaa pyydetyn määrän pelaajia maalien mukaan järjestettynä."""
        result = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in result],
            ["Player Two", "Player One"],
        )


if __name__ == "__main__":
    unittest.main()
