from .tactic import Tactic 

class MercedesCharge(Tactic):
    @property
    def name(self):
        return "Marcedes Charge"
    
    @property
    def fuel_cost(Self):
        return 90
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        opponent.tire_health -= 22
        opponent.turn_damage += 22