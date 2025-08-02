from driver import Driver
from tactics import DrsBoost, RedBullSurge, PrecisionTurn
from tactics import BrakeLate, ErsDeployment

class Max(Driver):
    def __init__(self):
        super().__init__("Max Verstappen")
        #the special moves of max verstappen
        self.offensive_moves = [
            DrsBoost(),
            RedBullSurge(),
            PrecisionTurn()
        ]

        self.defensive_moves = [
            BrakeLate(),
            ErsDeployment()
        ]
