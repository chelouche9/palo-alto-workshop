# Create a service class that receives one of the logger classes.
# Create 2 services using each of the loggers and use them.
class ILogger:
    def log(self, message: str):
        pass

class ConsoleLogger(ILogger):
    def log(self, message: str):
        print(message)

class FileLogger(ILogger):
    def __init__(self, file: str):
        self.file = file
    
    def log(self, message: str):
        with open(self.file, 'a') as f:
            f.write(f'{message}\n')