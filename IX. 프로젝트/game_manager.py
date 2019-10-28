from tictactoe import TicTacToe

class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        # 게임판 보여주기
        print(self.ttt)
        # row, col 입력받기
        self.ttt.set(1,1)
        # check_winner 면 끝내기


if __name__ == "__main__":
    gm = GameManager()
    gm.play()