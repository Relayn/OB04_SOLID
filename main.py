from abc import ABC, abstractmethod


class Weapon(ABC):
    """Абстрактный класс для оружия."""

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    """Класс меча."""

    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    """Класс лука."""

    def attack(self):
        return "Боец стреляет из лука."


class Fighter:
    """Класс бойца."""

    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"{self.name} выбирает новое оружие.")

    def attack(self, monster: 'Monster'):
        print(self.weapon.attack())
        monster.take_damage(20)  # Условный урон


class Monster:
    """Класс монстра."""

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print(f"Монстр {self.name} побежден!")
        else:
            print(f"Монстр {self.name} получил урон. Осталось здоровья: {self.health}.")

# Создаем оружие
sword = Sword()
bow = Bow()

# Создаем бойца
fighter = Fighter("Воин", sword)

# Создаем монстра
monster = Monster("Орк", 40)

# Бой
fighter.attack(monster)  # Боец наносит удар мечом.
fighter.change_weapon(bow)  # Воин выбирает новое оружие.
fighter.attack(monster)  # Боец наносит удар из лука.
