# <-----Task 1-----> #
#Declare character variables
wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"

#Declare Hp Variables
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

#Declare Damage Variables
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

# <-----Task 2-----> #
#user inputs
print("1) Wizard\n2) Elf \n3) Human")
character=input("Choose your character: ")

# <-----Task 3-----> #
#user inputs effect 1
while True:
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("You have chosen the character: ", character) 
        print("Health: ", my_hp)
        print("Damage: ", wizard_damage)
        break

    if character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("You have chosen the character: ", character) 
        print("Health: ", my_hp)
        print("Damage: ", elf_damage)
        break      

    if character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage        
        print("You have chosen the character: ", character) 
        print("Health: ", my_hp)
        print("Damage: ", human_damage)
        break  

    else:
        print("Unknown Character. Choose 1-3.")

# <-----Task 4-----> #
#While loop for Dragon battle
while True:
    dragon_hp = dragon_hp - my_damage
    print("\nThe", character, "damaged the Dragon!", "\nDragon HP: ", dragon_hp)
    if dragon_hp == 0:
        print("The Dragon has lost the battle.")
        break

    my_hp = my_hp - dragon_damage
    print("\nDragon strikes back.", "\nThe ", character, "'s HP: " , my_hp)

    if my_hp ==0:
        print("The ", character, " has lost the battle.")
        break

    
