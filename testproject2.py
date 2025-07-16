import random
answer = random.randint(1, 100)
attempts = 0
max_attempts = 10



while attempts < max_attempts:
    user_answer = int(input("Guess a number 1-100:"))
    attempts += 1
    difference = abs(user_answer - answer)

    if user_answer == answer:
        print("Correct!")
        print("You got it in", attempts, "attempts")
        break
    elif user_answer > answer:
        if difference <= 5:
            print("You're close!")
        print("too high")
    else:
      if difference <= 5:
        print("You're close!")
      print("too low")







