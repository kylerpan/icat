def computer(pile):
    choice = ""

    for n in pile:
        if n % 2 == 0:
            choice = choice + "0"
        else:
            choice = choice + "1"

    if choice == "0000":
        choice = ""
        for n in pile:
            if n != 0:
                choice = choice + "1"
            else:
                choice = choice + "0"

    return choice

def update(pile, choice):
    for n in range(4):
        pile[n] -= int(choice[n])
    print(pile)

# check if four piles
while True:
    pile = input("How much are in each pile? (ex. 1001 as [1, 0, 0, 1])  ")

    if len(pile) != 4:
        print("***You need four piles in order to play the game!***\n")
        continue

    break

pile_list = []
for n in pile:
    pile_list.append(int(n))

# check if first or second
while True:
    first_or_second = int(input("\nDo you want to go first or second? (1 or 2)  "))

    if first_or_second == 1 or first_or_second == 2:
        break
    else:
        print("***You have to choose 1 or 2!***")
        continue

# the game
while sum(pile_list) > 0:
    if first_or_second == 1:

        # player conditions
        while True:
            pick = input("\nHow many do you want to pick? (ex. 1001 as [1, 0, 0, 1])  ")

            if len(pick) != 4:
                print("***You must input 4 values!***")
                continue
            elif pick == "0000":
                print("***You have to pick from one pile!***")
                continue

            invalid = False
            for n in range(4):
                if int(pick[n]) > 1:
                    print("***You can't pick more than one from each pile!***")
                    invalid = True
                    break
                elif pile_list[n] - int(pick[n]) < 0:
                    print("***You can't take from a pile with 0!***")
                    invalid = True
                    break
                    
            if invalid == True:
                continue
            
            update(pile_list, pick)
            break
            
        if sum(pile_list) == 0:
            print("\nYou win!")
            break
        
        # computer's turn
        computer_pick = computer(pile_list)
        print(f"The computer picks this {computer_pick}")
        update(pile_list, computer_pick)

        if sum(pile_list) == 0:
            print("\nThe computer wins!")
            break

    elif first_or_second == 2:

        # computer's turn
        computer_pick = computer(pile_list)
        print(f"\nThe computer picks this {computer_pick}")
        update(pile_list, computer_pick)

        if sum(pile_list) == 0:
            print("\nThe computer wins!")
            break

        # player conditions
        while True:
            pick = input("\nHow many do you want to pick? (ex. 1001 as [1, 0, 0, 1])  ")

            if len(pick) != 4:
                print("***You must input 4 values!***")
                continue
            elif pick == "0000":
                print("***You have to pick from one pile!***")
                continue

            invalid = False
            for n in range(4):
                if int(pick[n]) > 1:
                    print("***You can't pick more than one from each pile!***")
                    invalid = True
                    break
                elif pile_list[n] - int(pick[n]) < 0:
                    print("***You can't take from a pile with 0!***")
                    invalid = True
                    break
                    
            if invalid == True:
                continue
            
            update(pile_list, pick)
            break


