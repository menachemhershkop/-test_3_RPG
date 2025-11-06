from abc import ABC, abstractmethod
class Fighters(ABC):
    def __init__(self,name:str,hp:float,speed:int,power:int,armor_rating:int):
        self.name=name
        self.hp=hp
        self.speed=speed
        self.power=power
        self.armor_rating=armor_rating
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def attack(self):
        pass