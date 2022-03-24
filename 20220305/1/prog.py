import readline
import shlex
import cmd


class repl(cmd.Cmd):
	prompt = '> '
	monsters = {}
	pcoord = (0,0)
	def do_add(self, arg):
		args = shlex.split(arg, comments=True)
		if len(args) == 8:
			m, n, name, h, hp, c, x, y = args
			if m == 'monster' and n == 'name' and h == 'hp' and c == 'coords' and hp.isdigit() and int(x) in range(10) and int(y) in range(10):
				hp = int(hp)
				x = int(x)
				y = int(y)
				if hp > 0:
					if name in self.monsters:
						self.monsters[name][(x, y)] = hp
					else:
						self.monsters[name] = {(x, y): hp}
				else:
					print('Add fail')
			else:
				print('Add fail')
		elif len(args) < 1:
			return
		else:
			print('Add fail')

	def do_show(self, arg):
		args = shlex.split(arg, comments=True)
		if len(args) == 1 and args[0] == 'monsters':
			for name, dct in self.monsters.items():
				for coords, hp in dct.items():
					print(f'{name} at ({coords[0]} {coords[1]}) hp {hp}')
		elif len(args) < 1:
			return
		else:
			print('Show fail')
	
	def do_move(self,arg):
		args = shlex.split(arg, comments=True)
		if len(args) == 1:
			match args[0]:
				case 'up':
					if self.pcoord[1] == 0:
						print('cannot move')
					else:
						self.pcoord = (self.pcoord[0], self.pcoord[1] - 1)
						print(f'player at {self.pcoord[0]} {self.pcoord[1]}')
						mons = ''
						for name, coord_and_hp in self.monsters.items():
							for coord, hp in coord_and_hp.items():
								if self.pcoord == coord:
									mons += f' {name} {hp} hp,'
						if len(mons) > 0:
							print('encountered:', mons[1:-1])
				case 'down':
					if self.pcoord[1] == 9:
						print('cannot move')
					else:
						self.pcoord = (self.pcoord[0], self.pcoord[1] + 1)
						print(f'player at {self.pcoord[0]} {self.pcoord[1]}')
						mons = ''
						for name, coord_and_hp in self.monsters.items():
							for coord, hp in coord_and_hp.items():
								if self.pcoord == coord:
									mons += f' {name} {hp} hp,'
						if len(mons) > 0:
							print('encountered:', mons[1:-1])
				case 'left':
					if self.pcoord[0] == 0:
						print('cannot move')
					else:
						self.pcoord = (self.pcoord[0] - 1, self.pcoord[1])
						print(f'player at {self.pcoord[0]} {self.pcoord[1]}')
						mons = ''
						for name, coord_and_hp in self.monsters.items():
							for coord, hp in coord_and_hp.items():
								if self.pcoord == coord:
									mons += f' {name} {hp} hp,'
						if len(mons) > 0:
							print('encountered:', mons[1:-1])
				case 'right':
					if self.pcoord[0] == 9:
						print('cannot move')
					else:
						self.pcoord = (self.pcoord[0] + 1, self.pcoord[1])
						print(f'player at {self.pcoord[0]} {self.pcoord[1]}')
						mons = ''
						for name, coord_and_hp in self.monsters.items():
							for coord, hp in coord_and_hp.items():
								if self.pcoord == coord:
									mons += f' {name} {hp} hp,'
						if len(mons) > 0:
							print('encountered:', mons[1:-1])
				case _:
					print("Move fail")
		elif len(args) < 1:
			return
		else:
			print('Move fail')

	def do_attack(self, arg):
		args = shlex.split(arg, comments = True)
		if len(args) == 1:
			if args[0] in self.monsters and self.pcoord in self.monsters[args[0]]:
				self.monsters[args[0]][self.pcoord] -= 10
				nowhp = self.monsters[args[0]][self.pcoord]
				if nowhp > 0:
					print(f'{args[0]} lost 10 hp, now has {nowhp} hp')
				else:
					print(f'{args[0]} dies')
					del self.monsters[args[0]]
			else:
				print(f'no {args[0]} here')
		elif len(args) < 1:
			return
		else:
			print('Attack fail')

	def complete_add(self, prefix, allcmd, beg, end):
		return [s for s in ["monster name", "coords"] if s.startswith(prefix)]
	def complete_show(self, prefix, allcmd, beg, end):
		return [s for s in ["monsters"] if s.startswith(prefix)]
	def complete_move(self, prefix, allcmd, beg, end):
		return [s for s in ["up", "down", "left", "right"] if s.startswith(prefix)]
	def complete_attack(self, prefix, allcmd, beg, end):
		mons = []
		for name, coord_and_hp in self.monsters.items():
			for coord, hp in coord_and_hp.items():
				if coord == self.pcoord:
					mons.append(name)
		return [s for s in mons if s.startswith(prefix)]
	def do_exit(self, arg):
		return True

repl().cmdloop()
