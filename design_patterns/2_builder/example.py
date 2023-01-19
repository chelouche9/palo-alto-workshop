class Computer:
    def __init__(self, cpu: str, memory: int, storage: int):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    def __str__(self):
        return f'CPU: {self.cpu}, Memory: {self.memory}, Storage: {self.storage}'

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('', 0, 0)

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self

    def set_memory(self, memory: int):
        self.computer.memory = memory
        return self

    def set_storage(self, storage: int):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer

# Create a ComputerBuilder object
builder = ComputerBuilder()

# Build a computer using the builder
computer = builder.set_cpu('Intel Core i7').set_memory(16).set_storage(1_000).build()

print(computer)  # Output: CPU: Intel Core i7, Memory: 16, Storage: 1000