import random

from core.goblin import Goblin
from core.orc import Orc
from cube.cube import Cube


class Game:
    def start(self):
        show_menu()
    def show_menu(self):
        print("לחץ 1 עבור מלחמה, לחץ 2 עבור יציאה")
    def choose_random_monster(self):
        monsters=[Orc,Goblin]
        choice_monster=random.choice(monsters)
        monster=choice_monster("נוני")
        print(monster.type)
        return monster
    def battle(self,player,monster):
        pass
    def roll_dice(self,sides):
        return Cube().rool(sides)
