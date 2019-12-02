from optparse import OptionParser


def init_teams(config):
    pass

def sim(config):
    teams = init_teams(config)
    year = config.start_year
    end_year = config.end_year

    market_types = {
        "std": Standard,
        "ca": CombinatorialAuction,
        "ttc": TopTradingCycle,
        "kidney": KidneyMatching,
        "call": CallAuction
    }

    market_class = market_types.get(config.market_type)

    market = market_class(teams, config)

    while year < end_year:
        market.run_year(year)

        year += 1


def main(args):
    usage_msg = "Usage: %prog [options]"

    def usage(msg):
        print "Error: %s\n" % msg
        parser.print_help()
        sys.exit()

    parser.add_option("--design",
                      dest="design", default="std",
                      help="Set the market design: 'std', 'ca', 'ttc', 'kidney', 'call'")

    parser.add_option("--teams",
                      dest="teams", default="nbateams.csv",
                      help="Set the teams in the league")

    parser.add_option("--players",
                      dest="players", default="nbaplayers.csv",
                      help="Set the players and years involved in the league")

    parser.add_option("init_assign",
                      dest="initial_assignment", default=None,
                      help="Assign players to teams pre-market")

    parser.add_option("start",
                      dest="start_year", default=2010,
                      help="Start year for the league trade market")

    parser.add_option("end",
                      dest="end_year", default=2019,
                      help="End year (not inclusive) for the league trade market")

    (options, args) = parser.parse_args()
