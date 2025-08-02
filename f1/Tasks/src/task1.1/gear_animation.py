import display_gear
import os
import time

def clear_screen():
    
    os.system("cls" if os.name == "nt" else "clear")

def animate_shift(from_gear, to_gear):
   
    # Display the current gear
    print(f"Current Gear: {from_gear}")
    display_gear.display_gear(from_gear)

    # Pause for realistic gear shift timing
    time.sleep(0.75)

    # Clear the screen 
    clear_screen()

    # Display the new gear
    print(f"New Gear: {to_gear}")
    display_gear.display_gear(to_gear)

def main():
    
    # Getting and validating from_gear input
    from_gear_input = input("Enter starting gear (0-8): ")
    from_valid, from_result = display_gear.validate_input(from_gear_input)

    if  not from_valid:
        print(f"Error: {from_result}")
        return

    # Getting and validating to_gear input
    to_gear_input = input("Enter target gear (0-8): ")
    to_valid, to_result = display_gear.validate_input(to_gear_input)

    if not to_valid:
        print(f"Error: {to_result}")
        return

    # Perform the animation
    print("\nStarting gear shift animation...")
    time.sleep(1) 
    clear_screen()
    animate_shift(from_result, to_result)
    """
    thought i really needed to add this cause skipping gears while accelerating
    isn't something that happens really ofter or maybe doesn't happen from a professional driver
    so no harm from a realistic funky output
    """

    #if the up shifiting skips more than two gears comment on the shifting
    if(to_result - from_result >= 2):
        print("do not skip gears while accelerating")
      


if __name__ == "__main__":
    main()
