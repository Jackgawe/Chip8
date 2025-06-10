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
## Fun Facts
- CHIP-8 was created in the 1970s for the COSMAC VIP computer
- The original CHIP-8 interpreter was written in machine code
- Modern CHIP-8 emulators can run games like Pong, Space Invaders, and Tetris
- The CHIP-8 display is monochrome and has a resolution of 64x32 pixels
- The CHIP-8 has 4KB of RAM, which is less than a single tweet

## Easter Eggs
- Try running the emulator with the flag `--debug` to see some cool debug info

## Contributing
Feel free to contribute to this project! Just don't break anything, please. I'm begging you.
## License
This project is licensed under the "Do Whatever You Want" license. Just don't blame me if your computer explodes.
## Acknowledgments
- The original CHIP-8 creators for making this awesome platform
- Special thanks to Nescafe.
- Shoutout to Andrew Newman for being a great debugging partner

## More Fun Facts
- The CHIP-8 interpreter was designed to be simple enough to be implemented on most computers of the time
- The original CHIP-8 had no sound capabilities, but modern emulators often add sound support
- The CHIP-8 instruction set consists of only 35 opcodes
- Some CHIP-8 games were used as educational tools to teach programming
- The CHIP-8's memory layout reserves the first 512 bytes (0x000-0x1FF) for the interpreter

## Technical Details
- The emulator runs at approximately 500Hz (500 instructions per second)
- The display is updated at 60Hz
- The CHIP-8's stack can hold up to 16 levels of nested subroutine calls
- The system uses a 16-bit program counter and 16 8-bit general-purpose registers
- The CHIP-8's display is drawn using XOR operations, which allows for sprite erasure

## Common Issues
- Some ROMs may not work due to timing differences between original hardware and emulation
- The original CHIP-8 had no standardized input handling, so key mappings may vary
- Some games may require specific timing to work correctly
- The emulator may not handle all edge cases perfectly
- Some ROMs may use undocumented features that aren't implemented
- Stuttery screen
- Controls aren't working on Windows, only Linux for some reason

## Future Plans
- Add support for Super CHIP-8 extensions
- Implement sound support
- Add more debugging features
- Improve timing accuracy
- Add support for save states

