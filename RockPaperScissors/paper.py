from interfaces import Strategy

class Paper(Strategy):
    def selection(self) -> str:
        return "Paper"