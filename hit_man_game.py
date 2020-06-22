import random
import time

from Objects_Blueprints import HitMan
from human_info import all_humans

print("""
Welcome to the Hit Man game. assassinate people until you have a Very high reputation or There is no one left to assassinate . That's it. Have fun!

When you forget who to assassinate, you can ask for the list but only three times.
The list will remain on the screen for a limited time, so take a quick look before it goes away.
When you get the list for the first time, it also disappears.

Assassinate the right people!
You get a penalty when you assassinate the wrong person. You have to pay $20.000
If you don't have enough money, it's Game Over!

type: `start` To start playing
 """)

commands = {
    'get-mission': "gets the mission to start assassinating ",
    'assassinate (first_name of the person)': "assassinate someone",
    'get-money': "gets your money",
    'get-assassination-list': "gets the list of people to assassinate",
    'get-assassinated': 'gets all the people you have assassinated',
    'get-reputation': 'gets your current reputation',
    'get-kills': 'tells how many people you assassinated',
}

# makes a list of human objects to be put on an assassination list
assassination_list = []
for i in range(15):
    assassination_list.append(random.choice(all_humans))

# makes it so that each Human in assassination_list is accessible by it's first_name
assassination_dict = {}
for i in assassination_list:
    assassination_dict[i.first_name] = i

player = HitMan('firstName lastName', 0, '1 1 2000', 'Male', 0, None)

start_command = input('>>>')

if start_command.lower() == 'start':
    print("the game has started!")
    print('\ntype: `help` To view the list of commands.')
    got_mission = False
    asked = int(len(assassination_list) / 3)
    people_assassinated = []
    while player.reputation != 'Very high':

        command = input('>>>')
        if command == 'help':
            for key, value in commands.items():
                print(f'--command:  {key}   ={value.center((len(value) + len(key) + len("--command:     =")))}')

        elif command == 'get-mission':
            if got_mission:
                print('You already got a mission')
            else:
                got_mission = True
                for i in assassination_list:
                    player.kill_list.append(i)
                for i in assassination_list:
                    print(f'''Born in {i.birth_date.strftime('%Y %B %d')}  --{i.first_name} {i.last_name}--. {i.his_her('3rdPers')} has ${i.money} in {i.his_her('possessive')} pocket.''')
                print(f'The list goes away in {len(assassination_list) / 2} seconds')
                time.sleep(len(assassination_list) / 2)
                print('\n' * 1000000)
                print('You got the list. Now you can start')

        elif command == 'get-assassination-list':
            if got_mission:
                asked -= 1
                if asked == 0:
                    print('You can\'t ask for the list anymore.')
                else:
                    print('TO ASSASSINATE:')
                    for key in assassination_dict:
                        print(f'-------{key}-------')
                    time.sleep(int(len(assassination_list) / 2))
                    print('\n' * 1000000)
            else:
                print('You need to get a mission first.')

        elif command.startswith('assassinate'):
            if got_mission:
                # it's just a letter e, sorry
                e = command.split()
                if len(e) == 1:
                    print('\tTHAT IS NOT A VALID NAME!')
                else:
                    name_victim = command.split()[1]
                    if not name_victim.capitalize().istitle():
                        print('\tTHAT IS NOT A VALID NAME!')
                    else:
                        name_victim = name_victim.capitalize()
                        try:
                            print(player.assassinate(assassination_dict[name_victim]))
                            people_assassinated.append(name_victim)
                            del assassination_dict[name_victim]
                            print(f'You have a {player.reputation} reputation')
                        except KeyError:
                            print(f'{name_victim} was not on the assassination list.')
                            print('$20.000 gets subtracted from the current amount of money you have')
                            player.money -= 20000
                            if player.money < 0:
                                print(f"${format(player.money+20000, ',').replace(',', '.')} is not enough to pay so")
                                print('\tGAME OVER!')
                                if len(assassination_dict) <= 3:
                                    print('You only had to assassinate: ')
                                    for val in assassination_dict.values():
                                        print(f'{val.first_name}+{val.last_name} {val.age} years old')
                                break
                            else:
                                print(f"You now have ${format(player.money, ',').replace(',', '.')}")

            else:
                print('You need to get a mission first!')
        elif command == 'get-money':
            print(f"you have ${format(player.money, ',').replace(',', '.')}")

        elif command == 'get-assassinated':
            if got_mission:
                for i in people_assassinated:
                    print(f'{i.center(100)}')
            else:
                print('Get the mission first!')

        elif command == 'get-reputation':
            print(f'Your reputation is {player.reputation}')

        elif command == 'get-kills':
            print(f'The amount of people you assassinated is {player.kills}')
        else:
            print('\tTHAT IS NOT A VALID COMMAND')

else:
    print('Oof something went wrong, You probably didn\'t type "start". Run the program again.')

with open('log_deaths.txt', 'a+') as file:
    file.write('\n+-----------------------------END OF LOG-----------------------------+\n')

print('\nCheck the log_deaths.txt file.'.upper())
