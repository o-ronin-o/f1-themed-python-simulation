from driver import Driver
from tactics import MercedesCharge, TurboStart, CornerMastery
from tactics import SlipstreamCut, AggressiveBlock

class Hassan(Driver):
    def __init__(self):
        super().__init__("Hassan Mostafa")
        #the special moves of hassan mostafa
        self.offensive_moves = [
            MercedesCharge(),
            TurboStart(),
            CornerMastery()
        ]

        self.defensive_moves = [
            SlipstreamCut(),
            AggressiveBlock()
        ]
