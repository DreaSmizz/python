"""
This is a template script. Please work off of this.
To test the functionality of the script as you build
it, you can run this by opening a terminal, using 
"cd risk_project_fellow" and then running 
"python risk.py".

Your name: Andrea Smith
Your e-mail: a.smith102781@gmail.com
Date finished: 10/13/2021
"""

# Step 1
# Collect the user's input. You can either use the
# argparse library for this (recommended) or the
# input() function.
# Step 2
# Simulate dice rolls to determine the output.
# Step 3
# Display the output to the user.
# To conform with our grader's required format, we've already 
# done this for you. Just make sure you set the number of 
# attackers remaining to the `attackers_remaining` variable and 
# the number of defenders remaining to the `defenders_remaining`
# variable in Step 2 of this script.
import random
import numpy as np

def attacker(attacker_dice):
    plays = 0
    if attacker_dice >= 3:
        plays = 3
    else:
        plays = attacker_dice
    
    attacker_plays = []
    for number in range(plays):
        attacker_plays.append(np.random.randint(1,6))
    return (attacker_plays)

def defender(defender_dice):
    plays = 0
    if defender_dice >= 2:
        plays = 2
    else:
        plays = defender_dice
        
    defender_plays = []
    for number in range(plays):
        defender_plays.append(np.random.randint(1,6))
    return (defender_plays)

def game_play(attacker_dice,defender_dice, count):
    attacker_count = attacker_dice
    defender_count = defender_dice
    game_on = True
    while game_on == True:
        if(attacker_count > count and defender_count > 0):
            attack = np.array(attacker(attacker_dice))
            defend = np.array(defender(defender_dice))
            #print(attack)
            #print(defend)
            if attack.size > 0 and defend.size > 0:
                a = attack[0]
                b = defend[0]
                if a > b:
                    attacker_count += 1
                    defender_count -= 1
                else:
                    attacker_count -= 1
                    defender_count += 1
            attack = np.delete(attack, 0)
            defend = np.delete(defend, 0)
            #print(attack)
            #print(defend)
            #print(f'Attacker: {attacker_count} remaining; Defender: {defender_count} remaining')
        else:
            game_on = False
    game_on = False
    print(f'Attacker: {attacker_count} remaining; Defender: {defender_count} remaining')
    
def main():
    attacker_dice = int(input("Number of attackers:"))
    defender_dice = int(input("Number of defenders:"))
    count = int(input("Number attack stops at:"))
    game_play(attacker_dice, defender_dice, count)

main()


# Step 4
# Run `python sanity_check.py` to confirm that your script
# handles inputs and outputs correctly