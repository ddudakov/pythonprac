"""Logic module."""


class Game():
    """Класс реализует основные игровые механики."""

    def __init__(self):
        """Эта функция инициализирует параметры Dungeon."""
        self.pcoord = (0, 0)
        self.monsters = []

    def add_monster(self, name, hp, crds):
        """Эта функция добавляет нового монстра в игру."""
        if not any([monster.name == name for monster in self.monsters]):
            self.monsters.append(Monster(name, hp, crds))
            print(self.monsters)
        elif not any([monster.crds == crds for monster in self.monsters if monster.name == name]):
            self.monsters.append(Monster(name, hp, crds))
        else:
            monster = [monster for monster in self.monsters if monster.name == name and monster.crds == crds][0]
            monster.hp = hp


class Monster():
    """Класс реализует характеристики монстров."""

    def __init__(self, name, hp, crds):
        """Параметры монстра."""
        self.name = name
        self.hp = hp
        self.crds = crds

    def __str__(self):
        """Эта функция выдает параметры монстров."""
        res = f'{self.name} at ({self.crds[0]} {self.crds[1]}) hp {self.hp}'
        return res
