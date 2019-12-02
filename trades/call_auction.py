from mechanism import Mechanism

class CallAuction(Mechanism):
    """
    Implements the call-auction trade mechanism
    """

    class Bid:
        """
        Contains information about a particular bid
        """
        def __init__(self, team, players, value):
            self.team = team
            self.players = players
            self.value = value


    class Ask:
        """
        Contains information about a particular ask
        """
        def __init__(self, team, players, value):
            self.team = team
            for player in players:
                if player not in self.team.players:
                    raise Exception("Team can only auction off owned players")
            self.players = players
            self.value = value


    def __init__(self, teams, config)
        super(CallAuction, self).__init__(teams, config)
        self.year_budget = config.budget
        self.team_budgets = {team.id: self.year_budget for team in self.teams}

        # auction_sets: list of player sets that are being auctioned
        # bids: bid lists corresponding to each auction_set
        # asks: ask lists corresponding to each auction_set
        self.auction_sets = []
        self.bids = []
        self.asks = []


    def clean_auctions(self):
        """
        Remove bids for players that a team already possesses and remove asks for players that
        a team no longer possesses
        """
        for i, (auction_set, bids, asks) in enumerate(zip(self.auction_set, self.bids, self.asks)):
            self.bids[i] = [bid for bid in bids if len(auction_set.intersection(bid.team.players)) == 0]
            self.asks[i] = [ask for ask in asks if auction_set.issubset(ask.team.players)]


    def clear_auctions(self):
        """
        Clear matched bids and asks from all player/player set auctions

        Return:
            cleared (bool): whether any clearances were made
        """
        cleared = False

        for auction_set, bids, asks in zip(self.auction_set, self.bids, self.asks):
            # only consider bids for which the team has enough budget remaining
            sorted_bids = sorted(
                [bid for bid in bids if bid.value < self.team_budgets[bid.team.id]],
                key=lambda bid: -bid.value
            )
            sorted_asks = sorted(asks, key=lambda ask: ask.value)

            if len(sorted_asks) == 0 or len(sorted_bids) == 0:
                continue

            top_ask = sorted_asks[0]

            if top_bid.value >= top_ask.value:
                self.move_players(top_ask.team, top_bid.team, auction_set)

                clearing_price = (top_ask.value + top_bid.value) / 2
                self.team_budgets[top_ask.team.id] += clearing_price
                self.team_budgets[top_bid.team.id] -= clearing_price

                cleared = True

        self.clean_auctions() # should clear used up bids/asks as well

        return cleared


    def reset_auctions(self):
        team_budgets = {team.id: self.year_budget for team in self.teams}
        self.auction_sets = []
        self.bids = []
        self.asks = []


    def run_year(self, year):
        self.reset_auctions()

        clearing = True

        while clearing:
            for team in self.teams:
                team.make_bids(team_budgets[team.id], self.teams)

            # teams will make asks based on bids
            for team in self.teams:
                team.make_asks(team_budgets[team.id], self.teams)

            clearing = self.clear_auctions()
