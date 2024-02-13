class Summoner:

    def __init__(self, name: str,  health: int, damage: int, mana: int) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana
        self.effects = []

    def take_damage(self, amount: int) -> bool:
        self.health -= amount
        return self.health > 0

    def take_effects(self):
        