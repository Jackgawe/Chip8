import sys
import pygame
import time
from cpu import CPU

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <rom_file>")
        sys.exit(1)
    
    # Initialize CPU
    cpu = CPU()
    
    # Load ROM
    try:
        cpu.load_rom(sys.argv[1])
    except FileNotFoundError:
        print(f"Error: ROM file '{sys.argv[1]}' not found.")
        sys.exit(1)
    
    # Main loop
    clock = pygame.time.Clock()
    while cpu.running:
        # Handle events
        for event in pygame.event.get():
            cpu.handle_event(event)
        
        # Execute CPU cycles
        # CHIP-8 typically runs at 500-700 Hz
        for _ in range(10):  # Execute multiple cycles per frame
            cpu.cycle()
        
        # Update display
        cpu.update_display()
        
        # Cap at 60 FPS
        clock.tick(60)
    
    # Cleanup
    cpu.cleanup()

if __name__ == "__main__":
    main() 