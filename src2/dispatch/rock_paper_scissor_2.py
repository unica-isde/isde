class Weapon:

    def __str__(self):
        return self.__class__.__name__

    def fight_against(self, other_weapon):
        return lookup_table[type(self), type(other_weapon)]


class Scissor(Weapon):
    pass


class Rock(Weapon):
    pass


class Paper(Weapon):
    pass


lookup_table = {(Scissor, Scissor): "TIE",
                (Scissor, Rock): "Rock",
                (Scissor, Paper): "Scissor",
                (Rock, Scissor): "Rock",
                (Rock, Rock): "TIE",
                (Rock, Paper): "Paper",
                (Paper, Scissor): "Scissor",
                (Paper, Rock): "Paper",
                (Paper, Paper): "TIE"}

if __name__ == '__main__':
    print("\n\n")
    list_of_weapons = [Scissor(), Paper(), Rock()]
    for w1 in list_of_weapons:
        for w2 in list_of_weapons:
            print(w1, 'vs', w2, '->', w1.fight_against(w2))
