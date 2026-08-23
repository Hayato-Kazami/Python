class Game:
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("=" * 20)
        print("Game Start")
        print("Game Over")
        print("=" * 20)

    @classmethod
    def show_top_score(cls):
        print(f"最高分：{cls.top_score}")

    def start_game(self):
        print(f"{self.player_name}开始游戏")

Game.show_help() #调用静态方法
Game.show_top_score()  #调用类方法

game = Game("LOL")
game.start_game()