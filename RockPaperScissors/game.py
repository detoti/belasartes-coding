from interfaces import Strategy
from randomi import Random
from paper import Paper

    
class Game:
    strategy: Strategy

    def __init__(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Random()

    def play(self, sec) -> None:
        s1 = self.strategy.selection()
        s2 = sec.strategy.selection()
        if s1 == s2:
            print("Draw - Play Again!")
        elif s1 == "Rock":
            if s2 == "Scissor":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif s1 == "Scissor":
            if s2 == "Paper":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif s1 == "Paper":
            if s2 == "Rock":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")


player1 = Game(Paper())

player2 = Game(Random())


player1.play(player2)