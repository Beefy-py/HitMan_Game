import random


class Citizen:
    def __init__(self, name, inventory=None):
        self.name = name
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory


class Player:
    hp = 10

    def __init__(self, name, inventory=None):
        self.name = name
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def steal_from(self, target):
        if not target:
            return 'The target does not exist'

        if not target.inventory:
            self.hp -= 1
            return f'{target.name} had nothing and you got busted!'
        item = random.choice(target.inventory)
        self.inventory.append(item)
        target.inventory.remove(item)
        return f'{self.name} has stolen a {item} from {target.name}'


citizen1 = Citizen('Lesly Shaw', ['Table', 'Phone', 'Knife'])
citizen2 = Citizen('William Vne')
player = Player('Beefy')

print(player.hp)
print(player.steal_from(citizen1))
print(player.inventory)
print(player.hp)
