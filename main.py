# Simple Game



class Creature:
    def __init__(self, name: str, hit_points: int, attack: int) -> None:
        self.name = name
        self.hit_points = hit_points
        self.attack = attack

    def take_damage(self, damage):
        self.hit_points -= damage

class Enemy(Creature):
    def __init__(self, name: str, hit_points: int, attack: int) -> None:
        super().__init__(name, hit_points, attack)

class Hero(Creature):
    def __init__(self, name: str, hit_points: int, attack: int) -> None:
        super().__init__(name, hit_points, attack)

class Sorcerer(Creature):
    def __init__(self, name: str, hit_points: int, attack: int, mana: int, spell_attack: int) -> None:
        super().__init__(name, hit_points, attack)
        self.mana = mana
        self.spell_attack = spell_attack

    def fire_bolt(self, power):
        if power > self.mana:
            raise Exception("not enough mana")
        self.attack = power
        self.mana -= power

def combat_round(attacker, defender):
    defender.take_damage(attacker.attack)
    print(f"{attacker.name} attacks {defender.name} for {attacker.attack} damage.")
    if defender.hit_points <= 0:
        raise Exception(f"{defender.name} is DEAD!")
    print(f"{defender.name} is down to {defender.hit_points} HP.")

def run_combat(first_combatant, second_combatant):
    try:
        combat_round(first_combatant, second_combatant)
        combat_round(second_combatant, first_combatant)
    except Exception as e:
        print(e)

goblin1: Enemy = Enemy("Goblin 1", 50, 3)
goblin2: Enemy = Enemy("Goblin 2", 50, 3)
fighter: Hero = Hero("Fighter", 100, 5)
sorcerer: Sorcerer = Sorcerer("Sorcerer", 75, 2, 100, 10)

combatants = {"Goblin 1": goblin1, "Goblin 2": goblin2, "Fighter": fighter, "Sorcerer": sorcerer}

print("Select combatants:")
i = 1
for key in combatants:
    print(f"{i} {key}")
    i += 1
for i in range(2):
    choice = input("\nChoose combatant {i}: ")
    combatant = combatants
    
print(f"\n{combatants[first_combatant]} vs {combatants[second_combatant]}")
print("\nRound 1: FIGHT!")
# combat_round(first_combatant, second_combatant)