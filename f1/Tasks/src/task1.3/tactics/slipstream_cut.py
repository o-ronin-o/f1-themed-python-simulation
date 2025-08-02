from .tactic import Tactic 

class SlipstreamCut(Tactic):
    @property
    def name(self):
        return "Slipstream Cut"
    
    @property
    def fuel_cost(Self):
        return 20
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        driver.tire_health += .4*driver.turn_damage
        opponent.turn_damage = 0
        