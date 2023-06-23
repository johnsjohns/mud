import random

class Character:
    def __init__(self, name, race, character_class, ability_scores):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.ability_scores = ability_scores

    def display_character(self):
        print("Name:", self.name)
        print("Race:", self.race)
        print("Class:", self.character_class)
        print("Ability Scores:", self.ability_scores)

def generate_ability_scores():
    abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    scores = {}

    for ability in abilities:
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        dice_rolls.sort(reverse=True)
        total = sum(dice_rolls[:3])
        scores[ability] = total

    return scores

def create_character():
    name = input("Enter character name: ")
    race = input("Enter character race: ")
    character_class = input("Enter character class: ")
    ability_scores = generate_ability_scores()

    character = Character(name, race, character_class, ability_scores)
    return character

def main():
    print("Dungeons & Dragons Character Creator")
    print("-----------------------------------")
    character = create_character()
    print("\nCharacter Created:")
    character.display_character()

if __name__ == "__main__":
    main()

