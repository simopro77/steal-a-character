# Complete Game Code

## Character Rarities
class Character:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

    def __repr__(self):
        return f'{self.name} ({self.rarity})'

# Rarity definitions
RARITIES = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']

## Gacha Mechanics
import random

class Gacha:
    def __init__(self):
        self.pool = []
        self.populate_pool()

    def populate_pool(self):
        for rarity in RARITIES:
            for i in range(5):  # 5 characters per rarity
                self.pool.append(Character(f'{rarity} Hero {i+1}', rarity))

    def draw(self):
        return random.choice(self.pool)

## Base System
class Game:
    def __init__(self):
        self.characters = []

    def summon(self, num=1):
        gacha = Gacha()
        for _ in range(num):
            character = gacha.draw()
            self.characters.append(character)

    def show_characters(self):
        for character in self.characters:
            print(character)

## Economy System
class Economy:
    def __init__(self):
        self.coins = 1000  # starting coins

    def earn_coins(self, amount):
        self.coins += amount

    def spend_coins(self, amount):
        if amount <= self.coins:
            self.coins -= amount
            return True
        return False

## Events
class Event:
    def __init__(self, name):
        self.name = name

    def trigger_event(self):
        print(f'Event triggered: {self.name}')

## Stealing Mechanics
class StealingMechanic:
    def __init__(self, players):
        self.players = players

    def steal_character(self, thief, victim):
        if victim.characters:
            stolen_character = random.choice(victim.characters)
            thief.characters.append(stolen_character)
            victim.characters.remove(stolen_character)
            print(f'{thief} stole {stolen_character} from {victim}')

# Example usage
if __name__ == '__main__':
    game = Game()
    game.summon(3)
    game.show_characters()
    economy = Economy()
    economy.spend_coins(100)
    event = Event('Lucky Draw')
    event.trigger_event()