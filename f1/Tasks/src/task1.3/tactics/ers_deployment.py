from .tactic import Tactic 

class ErsDeployment(Tactic):
    def __init__(self):
        super().__init__()
        self.attemps = 3
    @property
    def name(self):
        return "ERS Deployment"
    
    @property
    def fuel_cost(Self):
        return 40
    
    def execute(self,driver,opponent):
        if self.attemps <= 0:
            print(f"{driver.name} has no attempts left for {self.name}.\n skipping turn.")
            return
        driver.fuel -= self.fuel_cost
        driver.tire_health += .5*driver.turn_damage
        opponent.turn_damage = 0
        self.attemps -= 1
        print(f"{self.name} remains active. {self.attemps} attempts left.")