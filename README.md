# Autoclicker

A simple autoclicker created with Python that allows you to configure the control key and delays between clicks.

## Installation

1. Make sure you have Python 3.x installed on your system
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Launch the program:
```bash
python main.py
```

2. Default configuration:
   - Control key: Ctrl
   - Delay between clicks: 10-20ms (random)
   - Minimum delay: 10ms
   - Use F7 key to completely exit the program

3. GUI features:
   - The autoclicker activates when holding down the control key
   - Delay configuration:
     - Minimum delay: minimum value between clicks (minimum 10ms)
     - Maximum delay: maximum value between clicks (must be ≥ minimum delay)
     - "Random delay" option: enables/disables random variation between min and max delays
   - The number of clicks performed is displayed in real-time
   - Ability to change the control key through the interface

## Notes

- Make sure you have the necessary permissions to control the mouse on your system
- On Linux, you may need to run the program with sudo privileges to access keyboard inputs
- The program includes a PyAutoGUI failsafe function
- The interface uses CustomTkinter for a modern and customizable design 