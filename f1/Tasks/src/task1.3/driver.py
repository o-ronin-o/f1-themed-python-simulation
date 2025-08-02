class Driver:
    def __init__(self,name):
            
            self.name = name
            self.fuel =500
            self.tire_health = 100
            self.offensive_moves= []
            self.defensive_moves= []
            self.turn_damage = 0

    def can_defend(self, tactic):
        # Check if the driver has enough fuel to use a defensive tactic
        return self.fuel >= tactic.fuel_cost

    def can_attack(self, tactic):
        # Check if the driver has enough fuel to use an offensive tactic
        return self.fuel >= tactic.fuel_cost


    def take_turn(self, opponent):
        #Main method called during the driver's turn.
        print(f"\n{self.name}'s Turn:")
        print("Choose action:")
        print("1: Offensive")
        print("2: Defensive")
        # validation for action choice
        while True:
            choice = input("> ").strip()
            if choice == "2" and not self.defensive_moves:
                print("No defensive moves available.")
            elif choice == "1" and not self.offensive_moves:
                print("No offensive moves available.")
            elif choice in ("1", "2"):
                break
            else:
                print("Invalid input. Try again.")
        # Select and validate the chosen tactic
        if choice == "2":
            tactic = self._select_tactic(self.defensive_moves)
            if not self.can_defend(tactic):
                print(f"Not enough fuel to defend! ({self.fuel} < {tactic.fuel_cost})")
                return
        else:
            tactic = self._select_tactic(self.offensive_moves)
            if not self.can_defend(tactic):
                print(f"Not enough fuel to attack! ({self.fuel} < {tactic.fuel_cost})")
                return

        print(f"{self.name} uses {tactic.name}!")
        tactic.execute(self, opponent)

    def _select_tactic(self, moves):
         # Display available tactics and get a valid user choice
        print("Select a tactic:")
        for i, move in enumerate(moves):
            print(f"{i + 1}: {move.name} (Fuel: {move.fuel_cost})")

        while True:
            try:
                idx = int(input("> ")) - 1
                if 0 <= idx < len(moves):
                    return moves[idx]
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Enter a number.")
