from .tactic import Tactic 

class AggressiveBlock(Tactic):
    @property
    def name(self):
        return "Aggressive Block"
    
    @property
    def fuel_cost(Self):
        return 35
    
    def execute(self,driver, opponent):
        driver.fuel -= self.fuel_cost
        driver.tire_health += driver.turn_damage
        opponent.turn_damage = 0
        