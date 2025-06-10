import pygame

class Keyboard:
    # CHIP-8 keypad layout:
    # 1 2 3 C
    # 4 5 6 D
    # 7 8 9 E
    # A 0 B F
    
    KEY_MAP = {
        pygame.K_1: 0x1, pygame.K_2: 0x2, pygame.K_3: 0x3, pygame.K_4: 0xC,
        pygame.K_q: 0x4, pygame.K_w: 0x5, pygame.K_e: 0x6, pygame.K_r: 0xD,
        pygame.K_a: 0x7, pygame.K_s: 0x8, pygame.K_d: 0x9, pygame.K_f: 0xE,
        pygame.K_z: 0xA, pygame.K_x: 0x0, pygame.K_c: 0xB, pygame.K_v: 0xF
    }
    
    def __init__(self):
        self.keys = [False] * 16  # CHIP-8 has 16 keys (0x0-0xF)
    
    def handle_event(self, event):
        """Handle keyboard events."""
        if event.type == pygame.KEYDOWN:
            if event.key in self.KEY_MAP:
                self.keys[self.KEY_MAP[event.key]] = True
        elif event.type == pygame.KEYUP:
            if event.key in self.KEY_MAP:
                self.keys[self.KEY_MAP[event.key]] = False
    
    def is_key_pressed(self, key: int) -> bool:
        """Check if a specific key is pressed."""
        if 0 <= key < 16:
            return self.keys[key]
        return False
    
    def get_pressed_key(self) -> int:
        """Get the first pressed key, or -1 if no key is pressed."""
        for i, pressed in enumerate(self.keys):
            if pressed:
                return i
        return -1 