# -----------------------------------------------
#  Formula 1 Turn-Based Racing Simulation 
#
# In this project, I built a two-player F1-style race simulator using object-oriented programming and the Strategy Design Pattern.
# Each driver selects offensive or defensive tactics in turns, with the outcome depending on tire health and fuel usage.
#
# Object-Oriented Principles Used:
#
# 1. Abstraction:
#    I created an abstract base class `Tactic` using Python’s `ABC` module.
#    This defines a contract that all tactic subclasses must follow (execute, name, fuel_cost),
#    hiding internal implementation details and exposing only essential behavior.
#
# 2. Inheritance:
#    I used inheritance for multiple components:
#    - All tactic classes inherit from the abstract `Tactic` interface.
#    - Drivers like `Hassan` and `Max` inherit from a shared `Driver` base class.
#
# 3. Polymorphism:
#    I used polymorphism to allow all tactics to be used interchangeably through the same interface.
#    Each tactic has its own unique behavior, but I can call `tactic.execute(driver, opponent)` regardless of its actual type.
#    Similarly, both drivers can call `take_turn()` and use their own tactic sets.
#
# 4. Encapsulation:
#    I encapsulated driver state inside the `Driver` class — fuel, tire health, and move lists are instance variables,
#    and the logic for taking a turn or executing a move is hidden inside methods like `take_turn()` and `can_attack()`.
#
#  Strategy Design Pattern:
#
# I applied the Strategy Design Pattern to handle racing tactics dynamically.
# Instead of hardcoding logic inside the `Driver` class, I separated tactics into their own classes
# (like `RedBullSurge`, `TurboStart`, `SlipstreamCut`, etc.), each implementing a shared interface (`Tactic`).
# This lets me plug in different strategies (offensive or defensive) for each driver at runtime.
# I can easily swap, extend, or limit available tactics without changing the core driver logic.
#
# How it all runs:
# - The Race class handles the loop and checks for race-ending conditions.
# - Each driver chooses tactics and executes them, consuming fuel and affecting tire health.
# - When a driver’s tires are destroyed or both players run out of fuel, the race ends.
#




from race import Race

def main():
    race = Race()
    race.run()

if __name__ == "__main__":
    main()
