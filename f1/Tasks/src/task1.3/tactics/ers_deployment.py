from .tactic import Tactic 

class ErsDeployment(Tactic):
    @property
    def name(self):
        return "ERS Deployment"
    
    @property
    def fuel_cost(Self):
        return 40
    
    def execute(self,driver,opponent):
        driver.fuel -= self.fuel_cost
        driver.tire_health += .5*driver.turn_damage
        opponent.turn_damage = 0