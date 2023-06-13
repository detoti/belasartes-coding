from interfaces import Strategy

class Rock(Strategy):
    def selection(self) -> str:
        return "Rock"