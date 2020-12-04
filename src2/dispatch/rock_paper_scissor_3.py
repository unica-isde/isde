class Weapon:

    possible_weapons = {"Paper", "Rock", "Scissor"}

    lookup_table = {("Scissor", "Scissor"): "TIE",
                    ("Scissor", "Rock"): "Rock",
                    ("Scissor", "Paper"): "Scissor",
                    ("Rock", "Scissor"): "Rock",
                    ("Rock", "Rock"): "TIE",
                    ("Rock", "Paper"): "Paper",
                    ("Paper", "Scissor"): "Scissor",
                    ("Paper", "Rock"): "Paper",
                    ("Paper", "Paper"): "TIE"
                    }

    def __init__(self, name):
        if name in self.possible_weapons:
            self.name = name
        else:
            raise ValueError(name, 'is not a possible weapon')

    def __str__(self):
        return self.name

    def fight_against(self, other_weapon):
        return self.lookup_table[self.name, other_weapon.name]


if __name__ == '__main__':
    print("\n\n")
    weapons = [ Weapon(name) for name in Weapon.possible_weapons ]
    for w1 in weapons:
        for w2 in weapons:
            print(w1, 'vs', w2, '->', w1.fight_against(w2))
