class Memory:
    def __init__(self):
        # CHIP-8 has 4KB of memory (4096 bytes)
        self.memory = bytearray(4096)
        
        # Load font data into memory (0x000-0x1FF)
        self._load_font_data()
    
    def _load_font_data(self):
        # CHIP-8 font data - each digit is 5 bytes
        font_data = [
            0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
            0x20, 0x60, 0x20, 0x20, 0x70,  # 1
            0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
            0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
            0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
            0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
            0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
            0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
            0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
            0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
            0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
            0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
            0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
            0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
            0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
            0xF0, 0x80, 0xF0, 0x80, 0x80   # F
        ]
        
        # Load font data into memory starting at 0x000
        for i, byte in enumerate(font_data):
            self.memory[i] = byte
    
    def write_byte(self, address: int, value: int):
        """Write a byte to memory at the specified address."""
        if 0 <= address < len(self.memory):
            self.memory[address] = value & 0xFF
    
    def read_byte(self, address: int) -> int:
        """Read a byte from memory at the specified address."""
        if 0 <= address < len(self.memory):
            return self.memory[address]
        return 0
    
    def write_word(self, address: int, value: int):
        """Write a word (2 bytes) to memory at the specified address."""
        if 0 <= address < len(self.memory) - 1:
            self.write_byte(address, (value >> 8) & 0xFF)
            self.write_byte(address + 1, value & 0xFF)
    
    def read_word(self, address: int) -> int:
        """Read a word (2 bytes) from memory at the specified address."""
        if 0 <= address < len(self.memory) - 1:
            return (self.read_byte(address) << 8) | self.read_byte(address + 1)
        return 0
    
    def load_rom(self, rom_data: bytes):
        """Load ROM data into memory starting at 0x200."""
        for i, byte in enumerate(rom_data):
            if 0x200 + i < len(self.memory):
                self.memory[0x200 + i] = byte 