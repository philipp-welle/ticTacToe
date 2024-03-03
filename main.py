import random
dict = {"a1": "",
        "a2": "",
        "a3": "",
        "b1": "",
        "b2": "",
        "b3": "",
        "c1": "",
        "c2": "",
        "c3": "",
        }
entries = ["X", "0"]
RUNNING = True

print("")
print("This is a game of Tic Tac Toe, you will be playing against the computer. You are 'X'")
print("You play the game by entering the position you want to place your 'X'")
print("The positions are the following\n")
print(f" a1 | a2 | a3 ")
print("----------")
print(f" b1 | b2 | b3 ")
print("----------")
print(f" c1 | c2 | c3 \n")

def check_win(dict):
    global RUNNING
    # win conditions for the game
    win_list_a = [dict["a1"], dict["a2"], dict["a3"]]
    win_list_b = [dict["b1"], dict["b2"], dict["b3"]]
    win_list_c = [dict["c1"], dict["c2"], dict["c3"]]
    win_list_d = [dict["a1"], dict["b1"], dict["c1"]]
    win_list_e = [dict["a2"], dict["b2"], dict["c2"]]
    win_list_f = [dict["a3"], dict["b3"], dict["c3"]]
    win_list_g = [dict["a1"], dict["b2"], dict["c3"]]
    win_list_h = [dict["a3"], dict["b2"], dict["c1"]]
    win_conditions = [win_list_a, win_list_b, win_list_c, win_list_d, win_list_e, win_list_f, win_list_g, win_list_h]
    for s in entries:  # for X and 0 check win conditions
        for i in win_conditions:
            if sum(s in n for n in i) == 3:  # if any win condition has 3 of the same entries, you win
                if s == "X":
                    print("\nCongratulations, you won!")
                elif s == "0":
                    print("\nSorry, you lost!")
                RUNNING = False
                return True
    if not "" in dict.values(): # when all dict values are filled and no one has won, end the game with no winner
        print("\nThere was no winner in this round!")
        RUNNING = False
        return True
    return False

while RUNNING:
    player = input("Enter your position: ")
    if player in dict: # check if it was a valid entry
        if dict[player] == "": # check if position is already taken
            dict[player] = "X" # place X in chosen position
            if not check_win(dict): # check player win
                while True:
                    computer = random.choice(list(dict.keys())) # give the computer a random position
                    if dict[computer] == "": # check if the random position is clear, if not generate a new position
                        dict[computer] = "0"
                        break
                check_win(dict)
            print(f"\n {dict["a1"]} | {dict["a2"]} | {dict["a3"]}")
            print("----------")
            print(f" {dict["b1"]} | {dict["b2"]} | {dict["b3"]}")
            print("----------")
            print(f" {dict["c1"]} | {dict["c2"]} | {dict["c3"]} \n")
        else:
            print("Sorry, this position is already taken, try another one.")
    else:
        print(f"Sorry, that was not a valid input, please try again.")

