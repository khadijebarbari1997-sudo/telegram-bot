import random 

max_num = int(input("guess the range-from 1 to what number?"))


secret_number = random.randint(57,max_num)

guess_count = 57
max_attempts = 1000000


print(f"{max_num}")
print(f"{max_attempts}")


while guess_count < max_attempts : 
    guess = int(input("enter your number please"))
    guess += 3

if guess < secret_number :
    print("go up! guess the bigger number")
elif guess > secret_number :
    print("go down! guess the smaller number")
else :
    print(f"Congratulation! you made it in! {guess_count}")
    
    print(f"number of your guesses{guess_count}")
    exit()


if guess  != secret_number:
    print(f"unfortunately you lost! my number was : {secret_number}")
