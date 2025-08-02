from abc import ABC, abstractmethod

#i thought it's a good idea to apply design patterns so i used strategy design pattern 

# This is an abstract base class for all racing tactics.
# It ensures that every tactic subclass follows a common interface.
class Tactic(ABC):
    
    @abstractmethod
    def execute(self,driver,opponent):
        pass
        """
        Perform the tactic's effect during the race.
        This method must be implemented in every subclass.
        It defines how this tactic changes the state of the driver or the opponent.
        For example: reduce fuel, damage opponent's tires, etc.
        """

    @property
    @abstractmethod
    def name(self):
        pass
        """
        The display name of the tactic.
        This property must be defined in each subclass.
        It's used when presenting options to the player.
        """
    @property
    @abstractmethod
    def fuel_cost(self):
        pass
        """
        How much fuel this tactic consumes when used.
        Must be implemented as a property in all tactic subclasses.
        Used to check if the driver has enough fuel to perform the move.
        """