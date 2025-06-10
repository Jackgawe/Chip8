from memory import Memory
from display import Display
from keyboard import Keyboard
import random
import pygame

class CPU:
    def __init__(self):
        self.memory = Memory()
        self.display = Display()
        self.keyboard = Keyboard()
        self.V = [0] * 16
        self.I = 0
        self.PC = 0x200
        self.SP = 0
        self.stack = [0] * 16
        self.delay_timer = 0
        self.sound_timer = 0
        self.running = True
    
    def load_rom(self, rom_path: str):
        with open(rom_path, 'rb') as f:
            rom_data = f.read()
        self.memory.load_rom(rom_data)
    
    def cycle(self):
        instruction = self.memory.read_word(self.PC)
        self.PC += 2
        self._execute_instruction(instruction)
        if self.delay_timer > 0:
            self.delay_timer -= 1
        if self.sound_timer > 0:
            self.sound_timer -= 1
    
    def _execute_instruction(self, instruction: int):
        opcode = (instruction & 0xF000) >> 12
        x = (instruction & 0x0F00) >> 8
        y = (instruction & 0x00F0) >> 4
        n = instruction & 0x000F
        nn = instruction & 0x00FF
        nnn = instruction & 0x0FFF
        
        if opcode == 0x0:
            if instruction == 0x00E0:
                self.display.clear()
            elif instruction == 0x00EE:
                self.PC = self.stack[self.SP]
                self.SP = (self.SP - 1) & 0xF
        elif opcode == 0x1:
            self.PC = nnn
        elif opcode == 0x2:
            self.SP = (self.SP + 1) & 0xF
            self.stack[self.SP] = self.PC
            self.PC = nnn
        elif opcode == 0x3:
            if self.V[x] == nn:
                self.PC += 2
        elif opcode == 0x4:
            if self.V[x] != nn:
                self.PC += 2
        elif opcode == 0x5:
            if self.V[x] == self.V[y]:
                self.PC += 2
        elif opcode == 0x6:
            self.V[x] = nn
        elif opcode == 0x7:
            self.V[x] = (self.V[x] + nn) & 0xFF
        elif opcode == 0x8:
            if n == 0x0:
                self.V[x] = self.V[y]
            elif n == 0x1:
                self.V[x] |= self.V[y]
            elif n == 0x2:
                self.V[x] &= self.V[y]
            elif n == 0x3:
                self.V[x] ^= self.V[y]
            elif n == 0x4:
                result = self.V[x] + self.V[y]
                self.V[0xF] = 1 if result > 0xFF else 0
                self.V[x] = result & 0xFF
            elif n == 0x5:
                self.V[0xF] = 1 if self.V[x] >= self.V[y] else 0
                self.V[x] = (self.V[x] - self.V[y]) & 0xFF
            elif n == 0x6:
                self.V[0xF] = self.V[x] & 0x1
                self.V[x] >>= 1
            elif n == 0x7:
                self.V[0xF] = 1 if self.V[y] >= self.V[x] else 0
                self.V[x] = (self.V[y] - self.V[x]) & 0xFF
            elif n == 0xE:
                self.V[0xF] = (self.V[x] & 0x80) >> 7
                self.V[x] = (self.V[x] << 1) & 0xFF
        elif opcode == 0x9:
            if self.V[x] != self.V[y]:
                self.PC += 2
        elif opcode == 0xA:
            self.I = nnn
        elif opcode == 0xB:
            self.PC = nnn + self.V[0]
        elif opcode == 0xC:
            self.V[x] = random.randint(0, 255) & nn
        elif opcode == 0xD:
            sprite = bytes(self.memory.memory[self.I:self.I + n])
            collision = self.display.draw_sprite(self.V[x], self.V[y], sprite)
            self.V[0xF] = 1 if collision else 0
        elif opcode == 0xE:
            if nn == 0x9E:
                if self.keyboard.is_key_pressed(self.V[x]):
                    self.PC += 2
            elif nn == 0xA1:
                if not self.keyboard.is_key_pressed(self.V[x]):
                    self.PC += 2
        elif opcode == 0xF:
            if nn == 0x07:
                self.V[x] = self.delay_timer
            elif nn == 0x0A:
                key = self.keyboard.get_pressed_key()
                if key != -1:
                    self.V[x] = key
                else:
                    self.PC -= 2
            elif nn == 0x15:
                self.delay_timer = self.V[x]
            elif nn == 0x18:
                self.sound_timer = self.V[x]
            elif nn == 0x1E:
                self.I = (self.I + self.V[x]) & 0xFFF
            elif nn == 0x29:
                self.I = self.V[x] * 5
            elif nn == 0x33:
                self.memory.write_byte(self.I, self.V[x] // 100)
                self.memory.write_byte(self.I + 1, (self.V[x] % 100) // 10)
                self.memory.write_byte(self.I + 2, self.V[x] % 10)
            elif nn == 0x55:
                for i in range(x + 1):
                    self.memory.write_byte(self.I + i, self.V[i])
            elif nn == 0x65:
                for i in range(x + 1):
                    self.V[i] = self.memory.read_byte(self.I + i)
    
    def handle_event(self, event):
        self.keyboard.handle_event(event)
        if event.type == pygame.QUIT:
            self.running = False
    
    def update_display(self):
        self.display.update()
    
    def cleanup(self):
        self.display.close() 