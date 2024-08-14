import random 

class Pokemon:
    '''Pokemon class'''

    def __init__(self, name, health = 50, power = 30, defense = 30):
        '''Pokemon(str(name), int(health), int(power), int(defense))
        creates a new Pokemon
        str(name): Pokemon's name
        int(health): Stamina the pokemon has, defaults to 50
        int(power): Pokemon's attack power, defaults to 30
        int(defense): Pokemon's defensive power, defaults to 30'''


        self.name = name

        self.health = health

        self.power = power

        self.defense = defense

    def __str__(self):
        '''str(Pokemon) -> str
        Displays pokemon's name and then its health, attack, and defense'''

        return str(self.name) + ' (' + str(self.health) + ')' + \
               '\n' + 'ATT: ' + str(self.power) + ' DEF: ' + str(self.defense)

    def calculate_damage(self, other):
        '''Pokemon.calculate_damage(other)
        calculates the possible damage a Pokemon could do to another Pokemon'''

        r = random.uniform(0.85, 1)

        return float((((2.4 * self.power)/other.defense) + 2) * r) 

    def attack(self, other):
        '''Pokemon.attack(other)
        attacks other Pokemon using the calculate damage method'''

        damage = int(round(self.calculate_damage(other), 1))

        other.health -= damage

        if other.health <= 0:
            other.health = 0
            faint_status = '\n' + str(other.name) + ' has fainted and is unable to continue.'
        else:
            faint_status = ''

        if damage > 6:
            return print(str(self.name) + ' does ' + str(damage) + ' damage! ' + 'It was very effective!' + str(faint_status))
        if damage < 3:
            return print(str(self.name) + ' does ' + str(damage) + ' damage! ' + 'It was not very effective...' + str(faint_status))
        if damage ==  3:
            return print(str(self.name) + ' does ' + str(damage) + ' damage. ' + 'It was somewhat effective.' + str(faint_status))
        else:
            return print(str(self.name) + ' does ' + str(damage) + ' damage! ' + str(faint_status))
                   
        
        
    

        
Pikachu = Pokemon('Pikachu')

print(Pikachu)

Bulbasaur = Pokemon('Bulbasaur', 3)

print(Pikachu.calculate_damage(Bulbasaur))

Pikachu.attack(Bulbasaur)

        
