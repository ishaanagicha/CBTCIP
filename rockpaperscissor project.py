while True:
    import random
    user_choice=int(input("enter your choice {0 for rock , 1 for paper , 2 for scissor}"))
    computer_choice=random.randint(0,2)
    print("computer choice:" , computer_choice)
    if computer_choice == user_choice:
        print("its a draw")
    elif(computer_choice == 0 and user_choice == 2):
        print("you loose!")
    elif(computer_choice == 2 and user_choice == 0):
        print("you win!")
    elif(user_choice>computer_choice):
        print("you win!")
    elif(computer_choice>user_choice):
        print("you loose!")

