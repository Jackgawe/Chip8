# CHIP-8 Emulator
A Python-based CHIP-8 emulator that's byte-sized (haha get it bite sized, byte sized, chips, ok nvm)

## Features

- Full CHIP-8 instruction set implementation
- Display using Pygame
- Keyboard input handling
- Sound support
- ROM loading capability

## Requirements

- Python 3.8+
- Pygame

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the emulator with a CHIP-8 ROM:
```bash
python main.py path/to/rom.ch8
```

## Controls
- 1-4, Q-R, A-F, Z-V: CHIP-8 keypad
- ESC: Quit emulator
- Quite buggy
## Project Structure

- `main.py`: Entry point and main emulator loop
- `cpu.py`: CHIP-8 CPU implementation
- `display.py`: Display handling using Pygame
- `keyboard.py`: Keyboard input handling
- `memory.py`: Memory management
- `rom_loader.py`: ROM loading functionality
