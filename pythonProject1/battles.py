import random
import math

# TODO: make non-temp variables local and use getters and setters to reinitialize temp using local variables


class Player:
    def __init__(self, p_name, p_hp, p_attack, p_defense, p_speed, p_stress, p_list):
        # stat variables
        self.name = p_name
        self.max_hp = p_hp
        self.temp_max_hp: int = p_hp
        self.temp_hp: int = p_hp
        self.attack = p_attack
        self.temp_attack: int = p_attack
        self.defense = p_defense
        self.temp_defense: int = p_defense
        self.speed = p_speed
        self.temp_speed: int = p_speed
        self.stress = p_stress
        self.special = p_list
        self.player_actions = []

# TODO: make non-temp variables local and use getters and setters to reinitialize temp using local variables


class Enemy:
    def __init__(self, e_name, e_hp, e_attack, e_defense, e_speed, e_stress, e_list):
        # stat variables
        self.name = e_name
        self.max_e_hp = e_hp
        self.temp_max_e_hp = e_hp
        self.temp_e_hp: int = e_hp
        self.attack = e_attack
        self.temp_e_attack: int = e_attack
        self.defense = e_defense
        self.temp_e_defense: int = e_defense
        self.speed = e_speed
        self.temp_e_speed: int = e_speed
        self.stress = e_stress
        self.enemy_actions = [e_list]


alex = Player("Alex", 50, 12, 8, 10, 10, [])

rove = Enemy("Rove-Claw", 15, 12, 2, 3, 0, [])

cultist = Enemy("Cultist", 20, 13, 6, 11, 10, [])


# general action functions
# TODO: create GUI for battler
def player_action(character, enemy):
    print()
    selection = 11
    while selection != "0" and selection != "1" and selection != "2" and selection != "3":
        print("0: Attack")
        print("1: Waltz")
        print("2: Rhapsody")
        print("3: Ballad")
        selection = input("Select an action (0-3): ")
        if selection == "0":
            player_attack(character, enemy)
        elif selection == "1":
            waltz(character)
        elif selection == "2":
            rhapsody(character)
        elif selection == "3":
            ballad(character)
        else:
            print("Invalid input. Select an action (0-3)")
    print()
    return selection


def player_attack(character, enemy):
    damage: int = character.temp_attack - enemy.temp_e_defense
    if damage < 0:
        damage = 0

    if damage >= 0:
        enemy.temp_e_hp -= damage
    else:
        raise ValueError("Cannot be negative")
    if enemy.temp_e_hp < 0:
        enemy.temp_e_hp = 0

    print(f"{character.name} bashes the {enemy.name} with their piano!")
    print(f"The {enemy.name} takes {damage} damage!")
    return damage, enemy.temp_e_hp


def waltz(character):
    character.temp_speed += 5
    print("Alex played an energizing waltz! Their speed increased!")
    return character.temp_speed


def rhapsody(character):
    character.temp_hp += 10
    if character.temp_hp > character.temp_max_hp:
        character.temp_hp = character.temp_max_hp
    print(f"{character.name} played an invigorating rhapsody!")
    print(f"{character.name} healed 10 HP!")
    print(f"{character.name}'s current HP is {character.temp_hp}")
    return character.temp_hp


def ballad(character):
    character.temp_attack += 5
    print("Alex played an inspiring ballad! Their strength increased!")
    return character.temp_attack


def enemy_attack(character, enemy):
    damage: int = int(enemy.temp_e_attack - character.temp_defense)
    if damage < 0:
        damage = 0
    if damage >= 0:
        character.temp_hp -= damage
    else:
        raise ValueError("Cannot be negative")
    if character.temp_hp < 0:
        character.temp_hp = 0
    return damage, character.temp_hp


# Rove Arm's combat sequence
def rove_combat(character, enemy):
    '''
    :param character: the Player object whose stats are being used for the battle
    :param enemy: the Enemy object whose stats are being used for the battle
    :return: None
    Creates a battle loop for the Rove fight which ends when the temp_hp of either the player or the enemy reaches 0
    '''

    battle = True
    while battle:

        if character.temp_speed >= enemy.temp_e_speed:
            player_action(character, enemy)
            if enemy.temp_e_hp <= 0:
                print(f"{enemy.name} has been defeated!")
                break

            rove_action(character, enemy)
            if character.temp_hp <= 0:
                print(f"{character.name} has been defeated! Game Over!")
                break
            print(f"Player hp = {character.temp_hp}")
            print(f"Enemy hp = {enemy.temp_e_hp}")

        else:
            rove_action(character, enemy)
            if character.temp_hp <= 0:
                print(f"{character.name} has been defeated! Game Over!")
                break

            player_action(character, enemy)
            if enemy.temp_e_hp <= 0:
                print(f"{enemy.name} has been defeated!")
                break
            print(f"Player hp = {character.temp_hp}")
            print(f"Enemy hp = {enemy.temp_e_hp}")

    # re-initializes non-temp_hp stats
    alex.temp_max_hp = alex.max_hp
    alex.temp_speed = alex.speed
    alex.temp_attack = alex.attack
    alex.temp_defense = alex.defense

    # Cultist's combat sequence
def cultist_combat(character, enemy):
    '''
    :param character: the Player object whose stats are being used for the battle
    :param enemy: the Enemy object whose stats are being used for the battle
    :return: None
    Creates a battle loop for the cultist fight which ends when the temp_hp of either the player or the enemy reaches 0
    '''

    # Creates a battle loop for the battle with the cultist
    battle = True
    while battle:

        if character.temp_speed >= enemy.temp_e_speed:
            player_action(character, enemy)
            if enemy.temp_e_hp <= 0:
                print(f"{enemy.name} has been defeated!")
                break

            cult_action(character, enemy)
            if character.temp_hp <= 0:
                print(f"{character.name} has been defeated! Game Over!")
                break

        else:
            cult_action(character, enemy)
            if character.temp_hp <= 0:
                print(f"{character.name} has been defeated! Game Over!")
                break

            player_action(character, enemy)
            if enemy.temp_e_hp <= 0:
                print(f"{enemy.name} has been defeated!")
                break
        print(f"Player hp = {character.temp_hp}")
        print(f"Enemy hp = {enemy.temp_e_hp}")

    # reinitializes non-temp_hp stats
    alex.temp_max_hp = alex.max_hp
    alex.temp_speed = alex.speed
    alex.temp_attack = alex.attack
    alex.temp_defense = alex.defense


# enemy actions
def rove_action(character, enemy):
    e_roll = random.randint(1, 20)
    # TODO: convert random generation and attack into their own functions to help with testing

    if e_roll < 10:
        calc = enemy_attack(character, enemy)
        damage = calc[0]
        enemy.temp_e_hp = calc[0]
        print(f"The {enemy.name} attacks!")
        print(f"{character.name} takes {damage} damage!")

    elif 10 <= e_roll < 17:
        damage = enemy.temp_e_attack * 1.5 - character.temp_defense
        damage = math.ceil(damage)
        if damage < 0:
            damage = 0
        character.temp_hp -= damage
        print(f"The {enemy.name} throws {character.name} across the room!")
        print(f"{character.name} takes {damage} damage!")

    elif 17 <= e_roll < 21:
        damage = enemy.temp_e_attack - character.temp_defense
        character.temp_attack -= 1
        if damage < 0:
            damage = 0
        character.temp_hp -= damage
        print(f"The {enemy.name} grabs {character.name} and squeezes them!")
        print(f"{character.name} takes {damage} damage!")


# Cult member's attacks and probabilities
def cult_action(character, enemy):
    e_roll = random.randint(1, 20)
    if e_roll < 10:
        calc = enemy_attack(character, enemy)
        damage = calc[0]
        enemy.temp_e_hp = calc[0]
        print(f"The {enemy.name} attacks!")
        print(f"{character.name} takes {damage} damage!")

    elif 10 <= e_roll < 17:
        damage = enemy.temp_e_attack - character.temp_defense
        character.temp_max_hp -= 1
        if damage < 0:
            damage = 0
        character.temp_hp -= damage
        print(f"The {enemy.name} throws {character.name} across the room!")
        print(f"{character.name} takes {damage} damage!")
        print(f"{character.name} is badly injured. Their Max HP is lowered!")


    elif 17 <= e_roll < 10:
        damage = enemy.temp_e_attack - character.temp_defense
        character.temp_defense -= 1
        if damage < 0:
            damage = 0
        character.temp_hp -= damage
        print(f"The {enemy.name} hacks at {character.name} with his saw!")
        print(f"{character.name} takes {damage} damage!")
        print(f"{character.name} is knocked off guard. Their defense is lowered!")

    elif e_roll == 20:
        damage = enemy.temp_e_attack * 1.7 - character.temp_defense
        damage = math.ceil(damage)
        if damage < 0:
            damage = 0
        character.temp_hp -= damage
        print(f"The {enemy.name} gores {character.name} with his saw!")
        print(f"Ouch! {character.name} takes {damage} damage!")


# action menu didn't work but this is how it would have been implemented
# def action_menu():
    # app = QtWidgets.QApplication(sys.argv)
    # Battle = QtWidgets.QMainWindow()
    # ui = Ui_Battle()
    # ui.setupUi(Battle)
    # Battle.show()
    # sys.exit(app.exec_())
