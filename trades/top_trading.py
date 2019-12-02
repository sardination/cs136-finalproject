from mechanism import Mechanism

class TopTradingCycle(Mechanism):
    """
    Implements the top trading cycle (TTC) trade mechanism
    """

    def __init__(self, teams, config):
        super(TopTradingCycle, self).__init__(teams, config)

        self.completed_trades = [] # list of player sets that have been traded
        self.preference_orders = {team.id: team.preference_ordering for team in self.teams}


    def clear_cycles(self, edges):
        """
        Perform trades given the trading edges indicated by team
        preferences

        Args:
            edges (dict of tuples): tuple format (target_team, player_set) indexed by requesting_team id

        Return:
            cleared (bool): True if any cycles have been cleared, False otherwise
        """

        cleared = False

        examined_teams = []
        for team in self.teams:
            if team in examined_teams:
                continue

            potential_cycle = []
            current_team = team
            while True:
                if current_team in potential_cycle:
                    # cycle detected, provide chain corresponding to the cycle
                    index = potential_cycle.index(current_team)
                    potential_cycle = potential_cycle[index:]
                    cleared = True
                    break

                if current_team in examined_teams:
                    potential_cycle = []
                    break

                potential_cycle.append(current_team)
                examined_teams.append(current_team)

                edge = edges[current_team.id]
                if edge is None:
                    potential_cycle = []
                    break

                target_team, player_set = edge
                current_team = target_team

            # clear the discovered cycle
            for cycle_team in potential_cycle:
                target_team, player_set = edges[cycle_team.id]
                self.move_players(target_team, cycle_team, player_set)
                self.remove_player_preferences(player_set)

        return cleared

    def remove_player_preferences(self, player_set):
        """
        Remove all preferences from team preference orders that contain
        players from the given player set

        Args:
            player_set (set of Players): set of players to be removed from preference orders
        """
        for team in self.teams:
            curr_pref_order = self.preference_orders[team.id]
            self.preference_orders[team.id] = [pref_set for pref_set in curr_pref_order
                if len(pref_set.intersection(player_set)) == 0]


    def run_year(self, year):
        """
        Operate multi-stage TTC until each team has reached
        a null state in their preference ordering
        """

        clearing = True

        while clearing:
            # Generate preference graph
            edges = {team.id: None for team in self.teams}
            for team in self.teams:
                team_prefs = self.preference_orders[team.id][0]
                if len(team_prefs) == 0:
                    continue

                top_preference = team_prefs[0]
                for target_team in self.teams:
                    if top_preference.issubset(target_team.players):
                        edges[team.id] = (target_team, top_preference)
                        break

            clearing = self.clear_cycles(edges)

