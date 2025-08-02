#Task1.1:
# This code is a simple representation of a 7-segment display for gears.

# we should have the postions of segments in the grid
SEGMENTS_POSITIONS = {
    "A":[(0,0), (0,1),(0,2),(0,3)],
    "B":[(1,3)],
    "C":[(3,3)],
    "D":[(4,0),(4,1),(4,2),(4,3)],
    "E":[(3,0)],
    "F":[(1,0)],
    "G":[(2,0),(2,1),(2,2),(2,3)]
}

# now i need to interface each number to the corresponding segements
GEAR_SEGMENTS = {
    0:{"A","F", "E", "B", "C","D"},
    1:{"B", "C"},
    2:{"A", "B", "G", "E", "D"},
    3:{"A", "B", "G", "C", "D"},
    4:{"F", "G", "B", "C"},
    5:{"A", "F", "G", "C", "D"},
    6:{"A", "F", "G", "E", "C", "D"},
    7:{"A", "B", "C"},
    8:{"A", "B", "C", "D", "E", "F", "G"}
}


#the display function

def display_gear(gear_number):
    #getting the required segment according to the number 
    required_segments = GEAR_SEGMENTS[gear_number]
    
    #initializing the grid using a nested loop
    grid =[[" " for i in range(4)] for i in range(5)]

    
    indices = []
    #building the grid using the coordinations 
    for segment in required_segments:
        indices += SEGMENTS_POSITIONS[segment].copy()

        
        if(gear_number == 0):
            indices.append((2,0))   
            indices.append((2,3))        
        elif(gear_number == 1):
            indices.append((0,3))   
            indices.append((2,3))        
            indices.append((4,3))
        elif(gear_number == 7):   
            indices.append((2,3))        
            

        for row,column in indices:
            grid[row][column] ="#"
    for row in grid:
        print("".join(row))

def validate_input(user_input):
    try:
        gear = int(user_input.strip())
        if 0 <= gear <= 8:
            return True, gear
        else:
            return False, f"Invalid gear: {gear}. Please enter 0-8."
    except ValueError:
        return False, f"Invalid input: '{user_input}'. Please enter a number 0-8."

    
def main():
    while True:
        user_input = input("Enter Gear (0-8): ")
        is_valid, result = validate_input(user_input)

        if is_valid:
           display_gear(result)
           break
        else:
            print(f"Error: {result}")
            print("Try again...")




if __name__ == "__main__":
   main()

   





