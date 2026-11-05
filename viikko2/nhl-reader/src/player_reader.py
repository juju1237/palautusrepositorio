import requests

from player import Player


class PlayerReader:  # pylint: disable=too-few-public-methods
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url, timeout=10)
        response.raise_for_status()
        return [Player(player_data) for player_data in response.json()]
