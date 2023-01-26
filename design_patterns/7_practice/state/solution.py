# You are a software engineer in a gaming company.
# You are tasked with creating the Character class.
# A character can fight, cast spell and run. 
# A character has different states: fighting, casting, running, walking (this was missing) and idle (default state).
# A character cannot: run when fighting and cast a spell when running and walking.
# Implement these actions based on their state restrictions and how they impact the state.
from abc import ABC, abstractmethod

class CharacterState(ABC):
    def __init__(self, character):
        self.character = character

    @abstractmethod
    def fight(self):
        pass

    @abstractmethod
    def cast_spell(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def idle(self):
        pass

class WalkingState(CharacterState):
    def fight(self):
        self.character.state = FightingState(self.character)

    def cast_spell(self):
        print("Can't cast spell while walking")

    def run(self):
        self.character.state = RunningState(self.character)
    
    def walk(self):
        print("Walking already in progress")
    
    def idle(self):
        self.character.state = IdleState(self.character)

class FightingState(CharacterState):
    def fight(self):
        print("Fighting already in progress")

    def cast_spell(self):
        self.character.state = CastingState(self.character)

    def run(self):
        print("Cannot run while fighting!")
    
    def walk(self):
        self.character.state = WalkingState(self.character)
    
    def idle(self):
        self.character.state = IdleState(self.character)

class CastingState(CharacterState):
    def fight(self):
        self.character.state = FightingState(self.character)

    def cast_spell(self):
        print("Spell casting in progress")

    def run(self):
        self.character.state = RunningState(self.character)

    def walk(self):
        self.character.state = WalkingState(self.character)
    
    def idle(self):
        self.character.state = IdleState(self.character)

class IdleState(CharacterState):
    def fight(self):
        self.character.state = FightingState(self.character)

    def cast_spell(self):
        self.character.state = CastingState(self.character)
    
    def walk(self):
        self.character.state = WalkingState(self.character)

    def run(self):
        self.character.state = RunningState(self.character)
    
    def idle(self):
        print("already in idle state")

class RunningState(CharacterState):
    def fight(self):
        self.character.state = FightingState(self.character)

    def cast_spell(self):
        print("Can't cast spell when walking")

    def run(self):
        print("Running already in progress")

    def walk(self):
        self.character.state = WalkingState(self.character)
    
    def idle(self):
        self.character.state = IdleState(self.character)

class Character:
    def __init__(self):
        self.state = IdleState(self)

    def fight(self):
        self.state.fight()

    def cast_spell(self):
        self.state.cast_spell()

    def run(self):
        self.state.run()

    def walk(self):
        self.state.walk()

harry_potter = Character()
harry_potter.walk()
harry_potter.cast_spell()
# Can't cast spell while walking
harry_potter.fight()
harry_potter.run()
# Cannot run while fighting!
harry_potter.walk()
harry_potter.cast_spell()
# Can't cast spell while walking