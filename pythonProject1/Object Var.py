from view import *


# Rove Arm's combat sequence
def rove_combat(character, enemy):
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


# Cult member's combat sequence
def cultist_combat(character, enemy):
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


# Rove Arm's attacks and probabilities
def rove_action(character, enemy):
    e_roll = random.randint(1, 20)
    if e_roll < 10:
        damage = enemy.temp_e_attack - character.temp_defense
        if damage < 0:
            damage = 0
        character.temp_hp -= damage
        print(f"The {enemy.name} attacks!")
        print(f"{character.name} takes {damage} damage!")

    elif 10 <= e_roll < 17:
        damage = enemy.temp_e_attack * 1.5 - character.temp_defense
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
        damage = enemy.temp_e_attack - character.temp_defense
        if damage < 0:
            damage = 0
        character.temp_hp -= damage
        print(f"The {enemy.name} attacks!")
        print(f"{character.name} takes {damage} damage!")

    elif 10 <= e_roll < 17:
        damage = enemy.temp_e_attack - character.temp_defense
        character.max_hp -= 1
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
        if damage < 0:
            damage = 0
        character.temp_hp -= damage
        print(f"The {enemy.name} gores {character.name} with his saw!")
        print(f"Ouch! {character.name} takes {damage} damage!")


def player_action(character, enemy):
    p_roll = random.randint(1, 20)
    if p_roll < 9:
        damage = character.temp_attack - enemy.temp_e_defense
        if damage < 0:
            damage = 0
        enemy.temp_e_hp -= damage
        print(f"{character.name} bashes the {enemy.name} with their piano!")
        print(f"The {enemy.name} takes {damage} damage!")

    elif 9 <= p_roll < 13:
        character.temp_speed += 5
        print("Alex played an energizing waltz! Their speed increased!")
    elif 13 <= p_roll < 16:
        character.temp_hp += 10
        if character.temp_hp > character.max_hp:
            character.temp_hp = character.max_hp
        print(f"{character.name} played an invigorating rhapsody!")
        print(f"{character.name} healed 10 HP!")
        print(f"{character.name}'s current HP is {character.temp_hp}")
    elif 16 <= p_roll < 20:
        character.temp_attack += 5
        print("Alex played an inspiring ballad! Their strength increased!")
    elif p_roll == 20:
        damage = character.temp_attack * 2 - enemy.temp_e_defense
        if damage < 0:
            damage = 0
        enemy.temp_e_hp -= damage
        print(f"{character.name} clubs the {enemy.name} extra hard!")
        print(f"Hell yeah! The {enemy.name} takes {damage} damage!")


def main():
    alex = Player("Alex", 50, 12, 8, 10, 10, [])

    rove = Enemy("Rove-Claw", 15, 12, 2, 3, 0, [])

    cultist = Enemy("Cultist", 20, 13, 6, 11, 10, [])

    rove_combat(alex, rove)
    cultist_combat(alex, cultist)


main()
