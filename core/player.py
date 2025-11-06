from core.fighters import Fighters
import random

class Player(Fighters):
    def __init__(self, name, hp, speed, power, armor_rating):
        super().__init__(name,hp,speed,power,armor_rating)
        self.hp=50
        self.profession=["לוחם", "מרפא"]
    def speak(self):
        print(self.name, "is cuming!")
    def attack(self):
        print(123)

