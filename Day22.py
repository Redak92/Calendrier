class Summoner:

    def __init__(self, name: str,  health: int, damage: int, mana: int, spells: list) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = 0
        self.mana = mana
        self.effects = []
        self.spells = spells

    def take_damage(self, amount: int) -> bool:
        self.health -= amount
        return self.health > 0

    def begin_turn(self):
        try:
            # Start-turn effects
            for index, effect in enumerate(self.effects):
                exec(effect)
                self.effects[index][1] -= 1
            self.effects = [effect for effect in self.effects if effect[1] > 0]
            # Spell Casting
            print(f"Current mana {self.mana}\nCurrent health {self.health}")
            if len(self.spells) == 1 and self.spells[0][1] <= self.mana:
                print(self.spells[0][0].__name__)
            else:
                for j, i in enumerate([spell for spell in self.spells if spell[1] <= self.mana]):
                    print(f'Sort {j + 1}: {i[0].__name__}, Coût {i[1]}')
                print(self.spells[int(input("Quel sort choisissez vous ?")) - 1][0].__name__)
        except:
            self.begin_turn()

class Player(Summoner):
    def __init__(self, name: str,  health: int, damage: int, mana: int) -> None:
        super().__init__(name, health, damage, mana, [(self.HealSpell, 50), (self.HealSpell, 60)])
    def HealSpell(self) -> None:
        self.take_damage(-12)
        self.mana -= 50


a = Player("Bastien", 100, 0, 100)
a.begin_turn()
a.begin_turn()

