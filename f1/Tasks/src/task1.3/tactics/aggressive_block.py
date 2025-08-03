from .tactic import Tactic 

class AggressiveBlock(Tactic):
    def __init__(self):
        super().__init__()
        self.attemps = 2
    @property
    def name(self):
        return "Aggressive Block"
    
    @property
    def fuel_cost(Self):
        return 35
    
    def execute(self,driver, opponent):
        if self.attemps <= 0:
            print(f"{driver.name} has no attempts left for {self.name}.\n skipping turn.")
            return
        driver.fuel -= self.fuel_cost
        driver.tire_health += driver.turn_damage
        opponent.turn_damage = 0
        self.attemps -= 1
        print(f"{self.name} remains active. {self.attemps} attempts left.")

        