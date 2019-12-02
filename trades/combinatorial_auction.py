from mechanism import Mechanism

class CombinatorialAuction(Mechanism):
    """
    Implements the combinatorial auction trade mechanism
    """

    def __init__(self, teams, config):
        super(CombinatorialAuction, self).__init__(teams, config)