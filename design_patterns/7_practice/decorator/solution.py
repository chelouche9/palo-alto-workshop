# You are a software engineer in a gaming company.
# You are tasked with creating the Character boosts decorator class.
# A character can fight, walk and jump. 
# If a character finds a magic bean and eats it he makes x2 damage, jump x2 higher and walk x2 faster.
class Character():
    def __init__(self, name) -> None:
        self.damage = 1000
        self.walk_speed = 3
        self.jump_height = 0.5
        self.name = name
    
    def jump(self):
        print(f'{self.name} is jumping {self.jump_height} meter high')
    
    def walk(self):
        print(f'{self.name} is walking at {self.walk_speed} kph')

    def fight(self):
        print(f'{self.name} is punching at power of {self.damage} newtons')

class MagicBean(Character):
    def jump(self):
        self.jump_height = self.jump_height * 2
        print(f'{self.name} is jumping {self.jump_height} meter high')
    
    def walk(self):
        self.walk_speed = self.walk_speed * 2
        print(f'{self.name} is walking at {self.walk_speed} kph')

    def fight(self):
        self.damage = self.damage * 2
        print(f'{self.name} is punching at power of {self.damage} newtons')


goku = Character("Goku")
goku.walk()
goku.fight()
goku.jump()

# Now with magic bean
pumped_goku = MagicBean(goku)
pumped_goku.walk()
pumped_goku.fight()
pumped_goku.jump()