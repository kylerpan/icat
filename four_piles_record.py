# where computer is a recorder

def update(pile, choice):
    for n in range(4):
        pile[n] -= int(choice[n])
    print(pile)

print("--- Four Piles ---")

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

# the game
while sum(pile_list) > 0:

    # player 1 conditions
    while True:
        pick = input("\nPlayer 1, How many do you want to pick? (ex. 1001 as [1, 0, 0, 1])  ")

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
        print("\nPlayer 1, You win!")
        break

    
    # player 2 conditions
    while True:
        pick = input("\nPlayer 2, How many do you want to pick? (ex. 1001 as [1, 0, 0, 1])  ")

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
        print("\nPlayer 2, You win!")
        break
    






