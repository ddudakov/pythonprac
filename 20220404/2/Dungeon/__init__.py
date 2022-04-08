"""Interface module."""

import shlex
import cmd
from Dungeon.logic import Game

dunge = Game()


class repl(cmd.Cmd):
    """Этот класс работает как командная строка для Данжа."""

    prompt = '> '

    def __init__(self, dunge):
        """Инициализация параметров repl."""
        super(repl, self).__init__()
        self.dunge = dunge

    def do_add(self, arg):
        """Эта функция создаёт новых монстров на игровом поле."""
        args = shlex.split(arg, comments=True)
        if len(args) == 8:
            m, n, name, h, hp, c, x, y = args
            if m == 'monster' and n == 'name' and h == 'hp' and c == 'coords' \
               and hp.isdigit() and int(x) in range(10) and int(y) in range(10):
                hp = int(hp)
                x = int(x)
                y = int(y)
                if hp > 0:
                    self.dunge.add_monster(name, hp, (x, y))
                else:
                    print('Add fail')
            else:
                print('Add fail')
        elif len(args) < 1:
            return
        else:
            print('Add fail')

    def do_show(self, arg):
        """Эта функция показывает всех монстров на поле с их характеристиками и местонахождением на игровом поле."""
        args = shlex.split(arg, comments=True)
        if len(args) == 1 and args[0] == 'monsters':
            for monster in self.dunge.monsters:
                print(str(monster))
        elif len(args) < 1:
            return
        else:
            print('Show fail')

    def do_move(self, arg):
        """Эта функция реализует передвижение игрока по игровому полю."""
        args = shlex.split(arg, comments=True)
        if len(args) == 1:
            match args[0]:
                case 'up':
                    if self.dunge.pcoord[1] == 0:
                        print('cannot move')
                    else:
                        self.dunge.pcoord = (self.dunge.pcoord[0], self.dunge.pcoord[1] - 1)
                        self.after_moving()
                case 'down':
                    if dunge.pcoord[1] == 9:
                        print('cannot move')
                    else:
                        self.dunge.pcoord = (self.dunge.pcoord[0], self.dunge.pcoord[1] + 1)
                        self.after_moving()
                case 'left':
                    if self.dunge.pcoord[0] == 0:
                        print('cannot move')
                    else:
                        self.dunge.pcoord = (self.dunge.pcoord[0] - 1, self.dunge.pcoord[1])
                        self.after_moving()
                case 'right':
                    if self.dunge.pcoord[0] == 9:
                        print('cannot move')
                    else:
                        self.dunge.pcoord = (self.dunge.pcoord[0] + 1, self.dunge.pcoord[1])
                        self.after_moving()
                case _:
                    print("Move fail")
        elif len(args) < 1:
            return
        else:
            print('Move fail')

    def after_moving(self):
        """Эта функция показывает новые координаты игрока после передвижения и монстров, находящихся в новой клетке."""
        print(f'player at {self.dunge.pcoord[0]} {self.dunge.pcoord[1]}')
        mons = ''
        for monster in self.dunge.monsters:
            if monster.crds == self.dunge.pcoord:
                mons += f' {monster.name} {monster.hp} hp,'
        if len(mons) > 0:
            print(f'encountered: {mons[1:-1]}')

    def do_attack(self, arg):
        """Эта функция реализует атаку игроком монстра."""
        args = shlex.split(arg, comments=True)
        if len(args) == 1:
            for monster in self.dunge.monsters:
                if args[0] == monster.name and self.dunge.pcoord == monster.crds:
                    monster.hp -= 10
                    if monster.hp > 0:
                        print(f'{args[0]} lost 10 hp, now has {monster.hp} hp')
                    else:
                        print(f'{args[0]} dies')
                        self.dunge.monsters.remove(monster)
                else:
                    print(f'no {args[0]} here')
        elif len(args) < 1:
            return
        else:
            print('Attack fail')

    def complete_add(self, prefix, allcmd, beg, end):
        """Эта функция предлагает автодополнение для add."""
        return [s for s in ["monster name", "coords"] if s.startswith(prefix)]

    def complete_show(self, prefix, allcmd, beg, end):
        """Эта функция предлагает автодополнение для show."""
        return [s for s in ["monsters"] if s.startswith(prefix)]

    def complete_move(self, prefix, allcmd, beg, end):
        """Эта функция предлагает автодополнение для move."""
        return [s for s in ["up", "down", "left", "right"] if s.startswith(prefix)]

    def complete_attack(self, prefix, allcmd, beg, end):
        """Эта функция предлагает автодополнение для attack."""
        mons = []
        for monster in self.dunge.monsters:
            if monster.crds == self.dunge.pcoord:
                mons.append(monster.name)
        return [s for s in mons if s.startswith(prefix)]

    def do_exit(self, arg):
        """Эта функция завершает игру."""
        return True


def main():
    """Эта функция дает возможность запускать Dungeon как пакет."""
    repl(dunge).cmdloop()
