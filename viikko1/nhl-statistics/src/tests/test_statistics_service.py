import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_matching_player(self):
        player = self.stats.search("Gretzky")

        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_when_no_player_matches(self):
        self.assertIsNone(self.stats.search("Unknown"))

    def test_team_returns_players_from_requested_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"],
        )

    def test_top_returns_requested_number_in_descending_point_order(self):
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"],
        )

    def test_top_sorts_by_goals(self):
        players = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"],
        )

    def test_top_sorts_by_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"],
        )

    def test_top_sorts_by_points_when_explicitly_requested(self):
        players = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"],
        )


if __name__ == "__main__":
    unittest.main()
