secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter your secret number : "))
    if guess == secret_number:
        print("You won!")
        break
    guess_count = guess_count + 1
else:
    print("You have failed!")
