import random

skills = ["Rock","Scissor","Paper"]
words = ["Computer","You","Won","Score"]

computer_score = 0
player_score = 0

def computer_random():
    rand_om = random.randrange(0,2)
    return rand_om

while True:
    try:
        print("\n\tPick:\n\t1. "+ skills[0] +"\n\t2. "+ skills[1] +"\n\t3. "+ skills[2] +"\n")
        player_choice = int(input("Enter Pick Number: "))
        if player_choice == 0:
            break

        tasking = computer_random()
        computer_choice = skills[tasking]

        print("\n"+ words[1] +": " + str(skills[(player_choice)-1]) + " <===> "+ words[0] +": " + str(skills[tasking]))
        if skills[(player_choice)-1] == skills[tasking]:
            print("\n\t\t\'It's a Tie\'")

            # 1 - 1 == 1 - 1  also 2 - 1 == 2 - 1  also 3 - 3 == 0
        if player_choice - 1 == (tasking - 1) or (player_choice - 3) == tasking:
            print("\n\t\t\'"+ words[1] +" "+ words[2] +"\'")
            player_score = player_score + 1

            # 2 - 2 == 0 also 3 - 2 == 1 also 1 - 1 == 2 - 2
        if (player_choice - 2) ==  tasking or player_choice - 1 == (tasking - 2):
            print("\n\t\t\'"+ words[0] +" "+ words[2] +"\'")
            computer_score = computer_score + 1

        print("\n"+ words[1] +" "+ words[3] +": " + str(player_score) + " <===> "+ words[0] +" "+ words[3] +": " + str(computer_score))

    except Exception as e:
        break


