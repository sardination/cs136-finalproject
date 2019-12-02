class Player:
    """League Player"""

    def __init__(self, id):
        self.id = id
        self.team = None

    def assign_team(self, team):
        self.team = team
        if self.team:
            self.team.players.add(self)