from mechanism import Mechanism

class TopTradingCycle(Mechanism):
    """
    Implements the top trading cycle (TTC) trade mechanism
    """

    def __init__(self, teams, config):
        super(TopTradingCycle, self).__init__(teams, config)