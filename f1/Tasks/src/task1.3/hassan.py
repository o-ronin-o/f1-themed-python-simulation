from driver import Driver
from tactics import MercedesCharge, TurboStart, CornerMastery
from tactics import SlipstreamCut, AggressiveBlock
import speech_recognition as sr

class Hassan(Driver):
    def __init__(self):
        super().__init__("Hassan Mostafa")
        #the special moves of hassan mostafa
        self.offensive_moves = [
            MercedesCharge(),
            TurboStart(),
            CornerMastery()
        ]

        self.defensive_moves = [
            SlipstreamCut(),
            AggressiveBlock()
        ]
    def get_voice_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for your command(defensive or offensive)...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand your voice.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        
        return None

    def take_turn(self, opponent):
        print(f"\n{self.name}'s Turn (Voice Control):")

        # Keep asking until user says "offensive" or "defensive"
        while True:
            action_cmd = self.get_voice_command()
            if not action_cmd:
                continue  # Retry listening

            if "offensive" in action_cmd:
                moves = self.offensive_moves
                break
            elif "defensive" in action_cmd:
                moves = self.defensive_moves
                break
            else:
                print("Please say 'offensive' or 'defensive' to begin your move.")

        # If no moves are available for that type, fallback or skip
        if not moves:
            print(f"No {action_cmd} moves available.")
            return

        # Keep asking until user says a tactic name from the list
        while True:
            print("Say the name of the tactic you want to use:")
            tactic_cmd = self.get_voice_command()
            if not tactic_cmd:
                continue  # Retry listening

            for tactic in moves:
                if tactic.name.lower() in tactic_cmd:
                    if self.fuel < tactic.fuel_cost:
                        print(f"Not enough fuel to use {tactic.name}.")
                        return
                    print(f"{self.name} uses {tactic.name}!")
                    tactic.execute(self, opponent)
                    return

            print("Tactic not recognized. Try again.")
