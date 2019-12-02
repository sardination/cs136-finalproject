from mechanism import Mechanism

import csv

class Standard(Mechanism):
    """
    Implements the standard team-to-team trade mechanism
    """
    def __init__(self, teams, config):
        super(Standard, self).__init__(teams, config)

        self.trade_history_folder = config.trade_history_folder

    def run_year(self, year): # TODO: this shouldn't take an argument, how to maintain current filename?
        """
        Use a preexisting record of per-year historic trades

        Args:
            trades_filename (str): filename for the specific year of trades
        """

        with open(trades_filename, 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                # read from file and execute trade - self.move_players
                continue
