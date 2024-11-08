class Character('Hero'):

    def Attack(self):
        print("Hero Attacks a Enemy with Weapon ")

class Weapon(Character):

    def Attack(self):
        print("Weapon Deals damage ")


Character_Weapon = Weapon()
Character_Weapon.Attack()

class Enemy:

    def Enemy(self):
        print("Enemy Lost Health")


class Damage():
    pass


Character = Weapon()
Character.Attack()
Damage.Enemy()

