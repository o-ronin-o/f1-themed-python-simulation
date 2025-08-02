from .tactic import Tactic 

class CornerMastery(Tactic):
    @property
    def name(self):
        return "Corner Mastery"
    
    @property
    def fuel_cost(Self):
        return 25
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        opponent.tire_health -= 7
        opponent.turn_damage += 7
        