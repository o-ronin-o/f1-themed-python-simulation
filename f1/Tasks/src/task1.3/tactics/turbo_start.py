from .tactic import Tactic 

class TurboStart(Tactic):
    @property
    def name(self):
        return "Turbo Start"
    
    @property
    def fuel_cost(Self):
        return 50
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        opponent.tire_health -= 10
        opponent.turn_damage += 10

    