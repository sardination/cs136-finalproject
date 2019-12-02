class Mechanism:
    """
    Operational abstract mechanism to be executed in the market
    to assign players to each team
    """

    def run_year(self, year):
        """
        Execute a year of trades on the given year

        Args:
            year (int): year to execute trades on
        """
        pass

    @staticmethod
    def move_players(source_team, target_team, players):
        """
        Move `players` from `source_team` to `target_team`

        Args:
            source_team (Team): team giving players
            target_team (Team): team receiving players
            players (list of Players): players being given by `source_team`
        """

        source_team.remove(players)
        target_team.add(players)