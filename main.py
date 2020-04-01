from renderer import ConsoleRenderer
from game import ChessGame

def main():
    renderer = ConsoleRenderer()
    game = ChessGame(renderer)
    game.run()

if __name__ == "__main__":
    main()