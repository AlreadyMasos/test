from framework.singleton import Singleton


class LoggerParser(metaclass=Singleton):
    LOGS = None

    def open_logs(self):
        with open(r'\tests\logs.txt', 'r') as fd:
            self.LOGS = fd.read()

    def get_logs(self):
        if self.LOGS is None:
            self.open_logs()
        return self.LOGS
