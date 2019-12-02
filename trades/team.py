class Team:
    """League Team"""

    def __init__(self, id):
        self.id = id
        self.players = set()

    def set_budget(self, budget):
        self.budget = budget

    def add_players(self, players):
        # self.players = players
        for player in self.players:
            self.players.add(player)
            player.team = self

    def remove_players(self, players):
        # remove_players should be called before the subsequent add_players
        for player in self.players:
            self.players.remove(player)
            player.team = None

    def set_preference_ordering(self, preference_ordering):
        self.preference_ordering = preference_ordering

    def set_valuations(self, valuations):
        self.valuations = valuations

    # def propose_direct_trade(self, teams):
    #     """
    #     Return a tuple proposing the most favored trade
    #     for the team given current makeups of other teams.
    #     Returns None if no trade desired.
    #     """

    #     # TODO: perhaps use a preexisting record of actual trades made
    #     return None

    def make_bids(self, budget, teams):
        """
        Make bids on players and sets of players

        Args:
            budget (int): budget that the team has remaining to bid for players
            teams (list of Teams): teams in the league
        """
