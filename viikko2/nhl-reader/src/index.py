from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    nationality = Prompt.ask("Nationality (e.g. FIN)").strip().upper()
    season = Prompt.ask("Season (e.g. 2024-25)").strip()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Players from {nationality} ({season})")
    table.add_column("Player", style="cyan", no_wrap=True)
    table.add_column("Team", style="purple")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    Console().print(table)


if __name__ == "__main__":
    main()
