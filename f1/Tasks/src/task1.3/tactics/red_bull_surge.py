from .tactic import Tactic 

class RedBullSurge(Tactic):
    @property
    def name(self):
        return "Red Bull Surge"
    
    @property
    def fuel_cost(Self):
        return 80
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        opponent.tire_health -= 20
        opponent.turn_damage += 20
        