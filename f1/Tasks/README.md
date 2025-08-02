# 🏎️ F1 Strategy Racing Game (Python)

## 🚀 Overview
This is a futuristic Formula 1 turn-based racing simulation written in Python. Two iconic drivers — Max Verstappen and Hassan Mostafa — battle it out using strategic offensive and defensive racing maneuvers. The game uses object-oriented design principles and includes voice-controlled moves via the Groq Speech-to-Text API.

- Max uses manual input (keyboard)
- Hassan uses **voice commands** to select tactics
- Each move consumes fuel and affects tire health
- The race ends when one player's tire health hits 0 or both are out of fuel

## 🎯 Features
- Turn-based gameplay with live input
- Modular design using:
  - Strategy Design Pattern for tactics
  - Abstraction, Encapsulation, Inheritance, and Polymorphism
- Speech recognition with Groq's Whisper model (via `groq` API)
- Clean class structure (Driver, Tactics, Race, etc.)

## 🛠️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/f1-racing-sim.git
   cd f1-racing-sim

```
pip install -r requirements.txt
```

## Usage
To run the application, execute the following command:

```
python src/main.py
```

## Testing
To run the tests, use the following command:

```
pytest tests/test_main.py
```

## Project Structure
```
f1-racing-sim/
├── Tasks/
│   └── src/
│       └── task1.3/
│           ├── main.py
│           ├── race.py
│           ├── driver.py
│           ├── hassan.py
│           ├── max.py
│           ├── tactics/
│           │   ├── __init__.py
│           │   ├── drs_boost.py
│           │   ├── turbo_start.py
│           │   └── ... (all 10 tactics)
│           └── stt_recognizer.py
├── requirements.txt
├── README.md

```

## Author
Your Name

## License
This project is licensed under the MIT License.
