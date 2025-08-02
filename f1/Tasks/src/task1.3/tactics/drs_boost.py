from .tactic import Tactic 

class DrsBoost(Tactic):
    @property
    def name(self):
        return "DRS Boost"
    
    @property
    def fuel_cost(Self):
        return 45
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        opponent.tire_health -= 12
        opponent.turn_damage += 12
        