from hassan import Hassan
from max import Max

class Race:
    def __init__(self):
         # Initialize the race with two driver instances
        self.driver1 = Max()
        self.driver2 = Hassan()

    def run(self):
        print(" Race begins!")
        # Main race loop — continues while both drivers have tires left
        while(True):
         
            self.driver1.take_turn(self.driver2)
            print(f"{self.driver1.name} tire health :{self.driver1.tire_health}")
            print(f"Fuel:{self.driver1.fuel}")
            print(f"{self.driver2.name} tire health :{self.driver2.tire_health}")
            print(f"\nFuel:{self.driver2.fuel}")
            if(self.driver2.tire_health <= 0):
                print(f"\noooh no {self.driver2.name} tire health is:{self.driver2.tire_health}\n the winner is {self.driver1.name}")
                break
           
            self.driver2.take_turn(self.driver1)
           
            print(f"{self.driver1.name} tire health :{self.driver1.tire_health}")
            print(f"Fuel:{self.driver1.fuel}")
            print(f"{self.driver2.name} tire health :{self.driver2.tire_health}")
            print(f"\nFuel:{self.driver2.fuel}")
           
            if(self.driver1.tire_health <= 0):
                print(f"\noooh no {self.driver1.name} tire health is:{self.driver1.tire_health}\n the winner is {self.driver2.name}")
                break

            if self.driver1.fuel < 25 and self.driver2.fuel < 25:
                print("\n Both drivers are out of usable fuel. Race ends in a draw!")
                break


        print("\nFinal race stats:")
        print(f"\n{self.driver2.name} tire health :{self.driver2.tire_health}")
        print(f"\nFuel:{self.driver2.fuel}")
        print(f"\n{self.driver1.name} tire health :{self.driver1.tire_health}")
        print(f"\nFuel:{self.driver1.fuel}")
               
        print("\nRace ends!")
