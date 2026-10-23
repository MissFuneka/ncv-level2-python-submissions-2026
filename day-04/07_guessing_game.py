secret_number = 12
attempts = 0
guess_correctly = False

while attempts < 5 and guess_correctly == False:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess_val = int(guess)
        if guess_val < 1 or guess_val>20:
            print("the correct range is 1 to 20")
        else:
            attempts += 1
            if guess_val == secret_number:
                print ("Congratulations, You Guess Correctly! ")
                guess_correctly = True
            elif guess_val < secret_number:
                print ("Too Low")
            else:
                print ("Too High")
    else:
        print ("enter a valid number")
if guess_correctly == False:
    print (f'Failed to guess. Secret number is {secret_number}')