from .tactic import Tactic 

class BrakeLate(Tactic):
    @property
    def name(self):
        return "Brake Late"
    
    @property
    def fuel_cost(Self):
        return 25
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        driver.tire_health += .3*driver.turn_damage
        opponent.turn_damage = 0
        