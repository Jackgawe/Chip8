import pygame
import numpy as np

class Display:
    def __init__(self, scale: int = 10):
        self.width = 64
        self.height = 32
        self.scale = scale
        self.buffer = np.zeros((self.height, self.width), dtype=bool)
        pygame.init()
        self.screen = pygame.display.set_mode((
            self.width * self.scale,
            self.height * self.scale
        ))
        pygame.display.set_caption("CHIP-8 Emulator")
        self.bg_color = (0, 0, 0)
        self.fg_color = (255, 255, 255)
    
    def clear(self):
        self.buffer.fill(False)
    
    def draw_sprite(self, x: int, y: int, sprite: bytes) -> bool:
        collision = False
        
        for row in range(len(sprite)):
            for col in range(8):
                if sprite[row] & (0x80 >> col):
                    pixel_x = (x + col) % self.width
                    pixel_y = (y + row) % self.height
                    
                    if self.buffer[pixel_y, pixel_x]:
                        collision = True
                    
                    self.buffer[pixel_y, pixel_x] ^= True
        
        return collision
    
    def update(self):
        surface = pygame.Surface((self.width, self.height))
        surface.fill(self.bg_color)
        
        for y in range(self.height):
            for x in range(self.width):
                if self.buffer[y, x]:
                    surface.set_at((x, y), self.fg_color)
        
        scaled_surface = pygame.transform.scale(
            surface,
            (self.width * self.scale, self.height * self.scale)
        )
        
        self.screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()
    
    def close(self):
        pygame.quit() 