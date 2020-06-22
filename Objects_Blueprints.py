from datetime import datetime as dt


class Human:
    is_alive = True

    def __init__(self, name, money, birth_date, gender):
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]
        self.money = money
        self.birth_date = birth_date
        self.gender = gender

    def __str__(self):
        return f'''
        {self.first_name} {self.last_name}
        was born in {self.birth_date.year}-{self.birth_date.month}-{self.birth_date.day}
        and is {dt.today().year - self.birth_date.year} years old.
        {self.first_name} has ${self.money}'''

    @property
    def age(self):
        return dt.today().year - self.birth_date.year

    def his_her(self, ps_form):
        if ps_form == 'possessive':
            if self.gender == 'Male':
                return 'His'
            return 'Her'
        elif ps_form == '3rdPers':
            if self.gender == 'Male':
                return 'He'
            return 'She'


class HitMan(Human):
    reputation = 'low'

    def __init__(self, name, money, birth_date, gender, kills, kill_list=None):
        super().__init__(name, money, birth_date, gender)
        self.name = name
        self.kills = kills
        if kill_list is None:
            self.kill_list = []
        else:
            self.kill_list = kill_list

        if self.kills <= 10:
            self.reputation = 'low'
        elif 10 < self.kills <= 15:
            self.reputation = 'medium'
        elif 15 < self.kills <= 25:
            self.reputation = 'high'
        elif self.kills > 30:
            self.reputation = 'Very high'

    def assassinate(self, target):
        if target not in self.kill_list:
            return 'Target is not on the list'
        elif target in self.kill_list:

            self.kills += 1

            if self.kills <= 5:
                self.reputation = 'low'
            elif 5 < self.kills <= 15:
                self.reputation = 'medium'
            elif 15 < self.kills <= 25:
                self.reputation = 'high'
            elif self.kills > 30:
                self.reputation = 'Very high'

            self.money += target.money

            tombstone = f'''

                        |____{target.first_name}'s journal____|
                        {target.first_name} {target.last_name} was a good person.
                        {target.first_name} has lived {target.age} years.
                        {target.first_name} had ${target.money} in {target.his_her} pocket.
        
                        _______________________________________
                '''
            with open('log_deaths.txt', 'a+') as log_file:
                log_file.seek(0)
                content = log_file.read()
                if tombstone not in content:
                    log_file.write(tombstone)

            return f'{target.first_name} has been assassinated!'

    @property
    def get_money_with_name(self):
        return f"{self.first_name} has ${format(self.money, ',').replace(',', '.')}"

