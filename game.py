import random

class Character:
    def __init__(self, name, strength, agility):
        self.name = name
        self.strength = strength
        self.agility = agility

    def __str__(self):
        return f"{self.name} [Strength: {self.strength}, Agility: {self.agility}]"

class Gacha:
    def __init__(self):
        self.characters = [
            Character("Warrior", 10, 5),
            Character("Mage", 5, 10),
            Character("Rogue", 7, 8),
            Character("Paladin", 8, 6),
        ]

    def draw(self):
        return random.choice(self.characters)

class Base:
    def __init__(self):
        self.defense = 10
        self.resources = 100

    def steal(self, strength):
        if strength > self.defense:
            self.resources -= 20
            return True
        return False

class Game:
    def __init__(self):
        self.gacha = Gacha()
        self.character = None
        self.base = Base()

    def menu(self):
        while True:
            print("\n1. Draw a Character")
            print("2. Steal from Base")
            print("3. Exit")
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.character = self.gacha.draw()
                print(f"You drew: {self.character}")
            elif choice == '2':
                if self.character:
                    success = self.base.steal(self.character.strength)
                    if success:
                        print("Steal successful!")
                    else:
                        print("Steal failed! Base defense is too high.")
                else:
                    print("You need to draw a character first!")
            elif choice == '3':
                print("Exiting game.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    game = Game()
    game.menu()