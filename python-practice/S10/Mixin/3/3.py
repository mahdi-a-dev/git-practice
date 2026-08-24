import logging

logging.basicConfig(level=logging.INFO)

class LoggerMixin:
    def log(self, method, args):
        logging.info(f"Method: {method}, Arguments: {args}")

class Math(LoggerMixin):
    def add(self, a, b):
        self.log("add", (a, b))
        return a + b


m = Math()
m.add(5, 6)
