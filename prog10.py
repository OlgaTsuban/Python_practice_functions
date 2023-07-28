from random import randint
def predict_num(num):
    count = 0
    goal = randint(0, num)
    while True:
        user_input = int(input(f"enter your number from 0 till {num}: "))
        count +=1
        if user_input > goal:
            print("smaller")
        elif user_input < goal:
            print("larger")
        else:
            print(f"you win, number of attempts {count}")
            break
predict_num(18)
