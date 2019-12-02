from mechanism import Mechanism

class CombinatorialAuction(Mechanism):
    """
    Implements the combinatorial auction trade mechanism
    """

    def __init__(self, teams, config):
        super(CombinatorialAuction, self).__init__(teams, config)


    def run_year(self, year):
        """
        Execute a VCG combinatorial auction using teams' valuations of sets of players
        A team that owns a certain player or set of players can assign no valuation to indicate
        that they are unwilling to give this player up for ANY trade. Teams that own players are
        given priority in keeping their own players.
        """
        pass