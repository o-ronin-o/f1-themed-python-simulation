from .tactic import Tactic 

class PrecisionTurn(Tactic):
    @property
    def name(self):
        return "precision Turn"
    
    @property
    def fuel_cost(Self):
        return 30
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        opponent.tire_health -= 8
        opponent.turn_damage += 8
        