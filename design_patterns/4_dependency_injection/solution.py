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

class Service:
    def __init__(self, logger: ILogger):
        self.logger = logger
    
    def do_something(self):
        self.logger.log('Doing something...')

console_logger = ConsoleLogger()

service = Service(console_logger)

service.do_something()

file_logger = FileLogger('log.txt')

service = Service(file_logger)

service.do_something()