import random

skills = ["Rock","Scissor","Paper"]

computer_score = 0
player_score = 0

def computer_random():
    rand_om = random.randrange(0,3)
    return rand_om

while True:
    try:
        print("\n\tPick:\n\t1. Rock\n\t2. Scissor\n\t3. Paper\n")
        player_choice = int(input("Enter Pick Number: "))
        if player_choice == 0:
            break

        tasking = computer_random()

        print("\nYou: " + str(skills[(player_choice)-1]) + " <===> Computer: " + str(skills[tasking]))
        if skills[(player_choice)-1] == skills[tasking]:
            print("\n\t\t\'It's a Tie\'")

            # 1 - 1 == 1 - 1  also 2 - 1 == 2 - 1  also 3 - 3 == 0
        if player_choice - 1 == (tasking - 1) or (player_choice - 3) == tasking:
            print("\n\t\t\'You Won\'")
            player_score = player_score + 1

            # 2 - 2 == 0 also 3 - 2 == 1 also 1 - 1 == 2 - 2
        if (player_choice - 2) ==  tasking or player_choice - 1 == (tasking - 2):
            print("\n\t\t\'Computer Won\'")
            computer_score = computer_score + 1

        print("\nYou Score: " + str(player_score) + " <===> Computer Score: " + str(computer_score))

    except Exception as e:
        break


