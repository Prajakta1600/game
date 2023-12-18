import matplotlib.pyplot as plt
import time
def greet():
    print("Hi user, welcome to game world \n")
    select() 

def select():
    print("which game would you like to play ? \n")
    print("Game 1 - smartquiz\n")
    print("Game 2 - Test your GK with quiz game\n")
    print("Game 3 - guess the number \n")
    choice=int(input("Please enter the game number that you want to play \n"))
    if choice==1:
        smartquiz()
    elif choice==2:
        GK_Quiz()
    elif choice==3:
        guess_the_number()
    else:
        print("sorry, this game does not exist \n")
        repeat()

def smartquiz():
    print("You have 3 choices as below\n")
    print("1. Addition\n")
    print("2. Substraction\n")
    print("3. Multiplication\n")
    choice=int(input("Please enter the game number that you want to play \n"))
    if choice==1:
        smartquizaddition()
    elif choice==2:
        smartquizsubstraction()
    elif choice==3:
        smartquizmultiplication()
    else:
        print("sorry, this game does not exist \n")
    repeat() 

#game addition
def smartquizaddition():
    print("Welcome to smart quiz game \n")
    print("Insrtuctions for the game \n")
    print("you will be provided with two numbers \n")
    print("you need to sum them and enter you answer within 10 seconds \n")
    print("after giving 5 correct answers you will win \n")
    print("Are you ready? \n")
    print("let's go \n")
    gameaddition()

def gameaddition():
    import random
    import time
    count=0
    score=0
    user=input("Please enter a letter to represent you \n")
    start1=time.time()
    file1=open("F:\project\smartquiz\Addition\graphics.txt",'a')
    file2=open("F:\project\smartquiz\Addition\graphics data.txt",'a')
    obj=open("F:\project\smartquiz\Addition\data.txt",'a')
    while count<5:
        a=random.randint(1,9)
        b=random.randint(1,9)
        sumation=a+b
        start=time.time()
        print("sum of ",a," and ",b," is \n")
        answer=int(input("enter your answer "))
        end=time.time()
        if end-start<10:
            count=count+1
            if answer==sumation:
                score=score+1
                if count==5:
                    if score==5:
                        end1=time.time()
                        rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end1-start1)," seconds for whole game"]
                        obj.writelines(rank)
                        list1=[user[0]]
                        file1.writelines(list1)
                        list2=[str(score)]
                        file2.writelines(list2)
                        print("Booyeah! You Won. Your score is ",score,"out of 5 and you took ",str(end1-start1)," seconds for whole game\n")
                    else:
                        end2=time.time()
                        rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end2-start1)," seconds for whole game"]
                        obj.writelines(rank)
                        list1=[user[0]]
                        file1.writelines(list1)
                        list2=[str(score)]
                        file2.writelines(list2)
                        print("You have now finished the game. You scored ",score,"out of 5 and you took ",str(end2-start1)," seconds for whole game\n")
                else:
                    pass
            else:
                print(":( Your answer is incorrect \n")
                if count==5:
                    end3=time.time()
                    rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end3-start1)," seconds for whole game"]
                    obj.writelines(rank)
                    list1=[user[0]]
                    file1.writelines(list1)
                    list2=[str(score)]
                    file2.writelines(list2)
                    print("You have now finished the game. You scored ",score,"out of 5 and you took ",str(end3-start1)," seconds for whole game\n")
                else:
                    pass
        else:
            print("timeup, better luck next time,you took ",end-start," you were supposed to do in 10 seconds \n")
            print("you scored ",score," out of 5 \n")
            end4=time.time()
            rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end4-start1)," seconds for whole game"]
            obj.writelines(rank)
            list1=[user[0]]
            file1.writelines(list1)
            list2=[str(score)]
            file2.writelines(list2)
            break
    obj.close()
    file1.close()
    file2.close()
    print("\nDo you want to see score of others")
    choice=int(input("press 0 for no and 1 for yes "))
    if choice==0:
        pass
    elif choice==1:
        print("\nDo you want to see score in form of graphics")
        choice1=int(input("press 0 for no and 1 for yes "))
        if choice1==0:
            a_file=open("F:\project\smartquiz\Addition\data.txt",'r')
            lines=a_file.read()
            print("score of others who played this game ")
            print(lines, " ")
            a_file.close()
        elif choice1==1:
            a_file1=open("F:\project\smartquiz\Addition\graphics.txt",'r')
            lines=a_file1.read()
            x=list(lines)
            a_file2=open("F:\project\smartquiz\Addition\graphics data.txt",'r')
            line=a_file2.read()
            y=list(line)
            plt.bar(x,y)
            plt.show()
            a_file1.close()
        else:
            print("Sorry I could not understant your choice")
    else:
        print("Sorry I could not understant your choice")
        repeat1()

def repeat1():
    rep=int(input("\ndo you want to repeat game ? press 0 for no and 1 for yes "))
    if rep==1:
        smartquizaddition()
    elif rep==0:
        print("thanks for playing \n")
        repeat()
    else:
        repeat1() 

#game substration 

def smartquizsubstraction(): 
    print("Welcome to smart quiz game \n") 
    print("Insrtuctions for the game \n") 
    print("you will be provided with two numbers \n") 
    print("you need to substract them and enter you answer within 10 seconds \n") 
    print("after giving 5 correct answers you will win \n") 
    print("Are you ready? \n") 
    print("let's go \n") 
    gamesubstraction() 

def gamesubstraction(): 
    import random 
    import time 
    count=0 
    score=0 
    user=input("Please enter a letter to represent you \n") 
    start1=time.time() 
    file1=open("F:\project\smartquiz\substraction\graphics.txt",'a') 
    file2=open("F:\project\smartquiz\substraction\graphics data.txt",'a') 
    obj=open("F:\project\smartquiz\substraction\data.txt",'a') 
    while count<5: 
        a=random.randint(1,9) 
        b=random.randint(1,9) 
        substraction=a-b 
        start=time.time() 
        print("substraction of ",a," and ",b," is \n") 
        answer=int(input("enter your answer ")) 
        end=time.time() 
        if end-start<10: 
            count=count+1 
            if answer==substraction: 
                score=score+1 
                if count==5: 
                    if score==5: 
                        end1=time.time() 
                        rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end1-start1)," seconds for whole game"] 
                        obj.writelines(rank) 
                        list1=[user[0]] 
                        file1.writelines(list1) 
                        list2=[str(score)] 
                        file2.writelines(list2) 
                        print("Booyeah! You Won. Your score is ",score,"out of 5 and you took ",str(end1-start1)," seconds for whole game\n") 
                    else: 
                        end2=time.time() 
                        rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end2-start1)," seconds for whole game"] 
                        obj.writelines(rank) 
                        list1=[user[0]] 
                        file1.writelines(list1)
                        list2=[str(score)] 
                        file2.writelines(list2) 
                        print("You have now finished the game. You scored ",score,"out of 5 and you took ",str(end2-start1)," seconds for whole game\n") 
                else: 
                    pass 
            else: 
                print(":( Your answer is incorrect \n") 
                if count==5: 
                    end3=time.time() 
                    rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end3-start1)," seconds for whole game"] 
                    obj.writelines(rank) 
                    list1=[user[0]] 
                    file1.writelines(list1) 
                    list2=[str(score)] 
                    file2.writelines(list2) 
                    print("You have now finished the game. You scored ",score,"out of 5 and you took ",str(end3-start1)," seconds for whole game\n") 
                else: 
                    pass 
        else: 
            print("timeup, better luck next time,you took ",end-start," you were supposed to do in 10 seconds \n") 
            print("you scored ",score," out of 5 \n") 
            end4=time.time() 
            rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end4-start1)," seconds for whole game"] 
            obj.writelines(rank) 
            list1=[user[0]] 
            file1.writelines(list1) 
            list2=[str(score)] 
            file2.writelines(list2) 
            break 
    obj.close() 
    file1.close() 
    file2.close() 
    print("\nDo you want to see score of others") 
    choice=int(input("press 0 for no and 1 for yes ")) 
    if choice==0: 
        pass 
    elif choice==1: 
        print("\nDo you want to see score in form of graphics") 
        choice1=int(input("press 0 for no and 1 for yes ")) 
        if choice1==0: 
            a_file=open("F:\project\smartquiz\substraction\data.txt",'r') 
            lines=a_file.read() 
            print("score of others who played this game ") 
            print(lines, " ") 
            a_file.close() 
        elif choice1==1: 
            a_file1=open("F:\project\smartquiz\substraction\graphics.txt",'r') 
            lines=a_file1.read() 
            x=list(lines) 
            a_file2=open("F:\project\smartquiz\substraction\graphics data.txt",'r') 
            line=a_file2.read() 
            y=list(line) 
            plt.bar(x,y) 
            plt.show() 
            a_file1.close() 
            a_file2.close() 
        else: 
            print("Sorry I could not understant your choice") 
    else: 
        print("Sorry I could not understant your choice") 
        repeat2() 

def repeat2(): 
    rep=int(input("\ndo you want to repeat game ? press 0 for no and 1 for yes ")) 
    if rep==1: 
        smartquizsubstraction() 
    elif rep==0: 
        print("thanks for playing \n") 
        repeat() 
    else: 
        repeat2() 

#game 3 multiplication 

def smartquizmultiplication(): 
    print("Welcome to smart quiz game \n") 
    print("Insrtuctions for the game \n") 
    print("you will be provided with two numbers \n") 
    print("you need to multiply them and enter you answer within 10 seconds \n") 
    print("after giving 5 correct answers you will win \n") 
    print("Are you ready? \n") 
    print("let's go \n") 
    gamemultiplication() 

def gamemultiplication(): 
    import random 
    import time 
    count=0 
    score=0 
    user=input("Please enter a letter to represent you \n") 
    start1=time.time() 
    file1=open("F:\project\smartquiz\multiplication\graphics.txt",'a') 
    file2=open("F:\project\smartquiz\multiplication\graphics data.txt",'a') 
    obj=open("F:\project\smartquiz\multiplication\data.txt",'a') 
    while count<5: 
        a=random.randint(1,9) 
        b=random.randint(1,9) 
        multiplication=a*b 
        start=time.time() 
        print("product of ",a," and ",b," is \n") 
        answer=int(input("enter your answer ")) 
        end=time.time() 
        if end-start<10: 
            count=count+1 
            if answer==multiplication: 
                score=score+1 
                if count==5: 
                    if score==5: 
                        end1=time.time() 
                        rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end1-start1)," seconds for whole game"] 
                        obj.writelines(rank) 
                        list1=[user[0]] 
                        file1.writelines(list1) 
                        list2=[str(score)] 
                        file2.writelines(list2) 
                        print("Booyeah! You Won. Your score is ",score,"out of 5 and you took ",str(end1-start1)," seconds for whole game\n") 
                    else: 
                        end2=time.time() 
                        rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end2-start1)," seconds for whole game"] 
                        obj.writelines(rank)
                        list1=[user[0]] 
                        file1.writelines(list1) 
                        list2=[str(score)] 
                        file2.writelines(list2) 
                        print("You have now finished the game. You scored ",score,"out of 5 and you took ",str(end2-start1)," seconds for whole game\n") 
                else: 
                    pass 
            else: 
                print(":( Your answer is incorrect \n") 
                if count==5: 
                    end3=time.time() 
                    rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end3-start1)," seconds for whole game"] 
                    obj.writelines(rank) 
                    list1=[user[0]] 
                    file1.writelines(list1) 
                    list2=[str(score)] 
                    file2.writelines(list2) 
                    print("You have now finished the game. You scored ",score,"out of 5 and you took ",str(end3-start1)," seconds for whole game\n") 
                else: 
                    pass 
        else: 
            print("timeup, better luck next time,you took ",end-start," you were supposed to do in 10 seconds \n") 
            print("you scored ",score," out of 5 \n") 
            end4=time.time() 
            rank=["\n",(user)," scored ",str(score)," out of 5 and took ",str(end4-start1)," seconds for whole game"] 
            obj.writelines(rank) 
            list1=[user[0]] 
            file1.writelines(list1) 
            list2=[str(score)] 
            file2.writelines(list2) 
            break 
    obj.close() 
    file1.close() 
    file2.close() 
    print("\nDo you want to see score of others") 
    choice=int(input("press 0 for no and 1 for yes ")) 
    if choice==0: 
        pass 
    elif choice==1: 
        print("\nDo you want to see score in form of graphics") 
        choice1=int(input("press 0 for no and 1 for yes ")) 
        if choice1==0: 
            a_file=open("F:\project\smartquiz\multiplication\data.txt",'r') 
            lines=a_file.read() 
            print("score of others who played this game ") 
            print(lines, " ") 
            a_file.close() 
        elif choice1==1: 
            a_file1=open("F:\project\smartquiz\multiplication\graphics.txt",'r') 
            lines=a_file1.read() 
            x=list(lines) 
            a_file2=open("F:\project\smartquiz\multiplication\graphics data.txt",'r') 
            line=a_file2.read() 
            y=list(line) 
            plt.bar(x,y) 
            plt.show() 
            a_file1.close() 
            a_file2.close() 
        else: 
            print("Sorry I could not understant your choice") 
    else:
        print("Sorry I could not understant your choice") 
        repeat3() 

def repeat3(): 
    rep=int(input("\ndo you want to repeat game ? press 0 for no and 1 for yes ")) 
    if rep==1: 
        smartquizmultiplication() 
    elif rep==0: 
        print("thanks for playing \n") 
        repeat() 
    else: 
        repeat3() 

 #game 4 GK_Quiz 

def GK_Quiz(): 
    x=0 
    print ("Welcome player \n") 
    print("you are now provided with some intresting general knowledge questions.\n") 
    print("These question include name of capital of different countries.\n") 
    print("Please enter your answers.\n") 
    user=input("Please enter a letter to represent you \n") 

    file1=open("F:\project\gk\graphics.txt",'a') 
    file2=open("F:\project\gk\graphics data.txt",'a') 
    obj=open("F:\project\gk\data.txt",'a') 

    print("\nWhat is the capital of Australia?") 
    Ans_1=input("a)Sydney\nb)Melbourne\nc)Brisbane\nd)Canberra\nYour answer is:") 
    if Ans_1.lower() == "d": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Canberra") 

    print("\nWhat is the capital of New Zealand?") 
    Ans_2=input("a)Auckland\nb)Wellington\nc)Hamilton\nd)Christchurch\nYour answer is:") 
    if Ans_2.lower() == "b": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Wellington") 

    print("\nWhat is the capital of Egypt?") 
    Ans_3=input("a)Cairo\nb)Alexandria\nc)Luxor\nd)Aswan\nYour answer is:") 
    if Ans_3.lower() == "a": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Cairo") 

    print("\nWhat is the capital of Germany?") 
    Ans_4=input("a)Munich\nb)Hamburg\nc)Berlin\nd)Cologne\nYour answer is:") 
    if Ans_4.lower() == "c": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Berlin") 

    print("\nWhat is the capital of Canada?") 
    Ans_5=input("a)Toronto\nb)Vancouver\nc)Montreal\nd)Ottawa\nYour answer is:") 
    if Ans_5.lower() == "d": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Ottawa") 

    print("\nWhat is the capital of Afghanistan?") 
    Ans_6=input("a)Kabul\nb)Herat\nc)Kandahar\nd)Kunduz\nYour answer is:") 
    if Ans_6.lower() == "a": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Kabul") 

    print("\nWhat is the capital of Japan?") 
    Ans_7=input("a)Osaka\nb)Kyoto\nc)Yokohama\nd)Tokyo\nYour answer is:") 
    if Ans_7.lower() == "d": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Tokyo") 

    print("\nWhat is the capital of South Korea?") 
    Ans_8=input("a)Busan\nb)Daegu\nc)Seoul\nd)Daejeon\nYour answer is:") 
    if Ans_8.lower() == "c": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Seoul") 

    print("\nWhat is the capital of Italy?") 
    Ans_9=input("a)Venice\nb)Rome\nc)Verona\nd)Florence\nYour answer is:") 
    if Ans_9.lower() == "b": 
        print ("Your answer is correct") 
        x = x + 1 
    else: 
        print("You are incorrect.\nThe correct answer is Rome") 

    rank = ["\n",(user)," scored ",str(x)," out of 9"] 
    obj.writelines(rank) 
    list1=[user[0]] 
    file1.writelines(list1) 
    list2=[str(x)] 
    file2.writelines(list2) 

    obj.close() 
    file1.close() 
    file2.close() 
    print("\nYou have finished game and you scored ",x," out of 9") 
    print("\nDo you want to see score of others") 
    choice=int(input("press 0 for no and 1 for yes ")) 
    if choice==0: 
        pass 
    elif choice==1: 
        print("\nDo you want to see score in form of graphics") 
        choice1=int(input("press 0 for no and 1 for yes ")) 
        if choice1==0: 
            a_file=open("F:\project\gk\data.txt",'r') 
            lines=a_file.read() 
            print("score of others who played this game ") 
            print(lines, " ") 
            a_file.close() 
        elif choice1==1: 
            a_file1=open("F:\project\gk\graphics.txt",'r') 
            lines=a_file1.read() 
            x=list(lines) 
            a_file2=open("F:\project\gk\graphics data.txt",'r') 
            line=a_file2.read() 
            y=list(line) 
            plt.bar(x,y) 
            plt.show() 
            a_file1.close() 
            a_file2.close() 
        else: 
            print("Sorry I could not understant your choice") 
    else: 
        print("Sorry I could not understant your choice") 
    repeat4() 

def repeat4(): 
    rep=int(input("\ndo you want to repeat game ? press 0 for no and 1 for yes ")) 
    if rep==1: 
        GK_Quiz() 
    elif rep==0: 
        print("thanks for playing \n") 
        repeat() 
    else: 
        repeat4()

 #game 5 guess_the_number 
 
def guess_the_number(): 
    import random 
    secret_number = random.randint(1,10) 
    print ("Welcome player \n") 
    print("you are now provided with one number,you need guess the number. \n") 
    print("Please enter any number between 1 and 10. \n") 
    print("Remember, you have only 5 attempts \n") 
    user=input("Please enter a letter to represent you \n") 
    total_guesses=0 
    obj=open("F:\project\guess the number\data.txt",'a') 
    file1=open("F:\project\guess the number\graphics.txt",'a') 
    file2=open("F:\project\guess the number\graphics data.txt",'a') 
    while total_guesses <=6 : 
        total_guesses = total_guesses +1 
        if total_guesses<=5: 
            guess = int(input("\nenter your guess ")) 
            if guess < secret_number: 
                print ("Your guess is below the number, please guess again ") 
            elif guess > secret_number: 
                print ("Your guess is above the number, please guess again ") 
            else: 
                print("\nYou have finished game and you took ",total_guesses," attempts to guess the number") 
                rank=["\n",(user)," took ",str(total_guesses)," to guess the correct number "] 
                obj.writelines(rank) 
                list1=[user[0]] 
                file1.writelines(list1) 
                list2=[str(total_guesses)] 
                file2.writelines(list2) 
                break 
        elif total_guesses ==6: 
            secret_number = str(secret_number) 
            print ("Nope, the number I was thinking was " , secret_number , ". \n") 
            rank=["\n",(user)," took 5 chances but could not guess the correct number. "] 
            obj.writelines(rank) 
            list1=[user[0]] 
            file1.writelines(list1) 
            list2=[str(5)] 
            file2.writelines(list2) 
        else: 
            break 
    obj.close() 
    file1.close() 
    file2.close() 
    print("\nDo you want to see score of others") 
    choice=int(input("press 0 for no and 1 for yes ")) 
    if choice==0: 
        pass 
    elif choice==1: 
        print("\nDo you want to see score in form of graphics") 
        choice1=int(input("press 0 for no and 1 for yes ")) 
        if choice1==0: 
            a_file=open("F:\project\guess the number\data.txt",'r') 
            lines=a_file.read() 
            print("score of others who played this game ") 
            print(lines, " ") 
            a_file.close() 
        elif choice1==1: 
            a_file1=open("F:\project\guess the number\graphics.txt",'r') 
            lines=a_file1.read() 
            x=list(lines) 
            a_file2=open("F:\project\guess the number\graphics data.txt",'r') 
            line=a_file2.read() 
            y=list(line) 
            plt.bar(x,y) 
            plt.show() 
            a_file1.close() 
            a_file2.close() 
        else: 
            print("Sorry I could not understant your choice") 
    else: 
        print("Sorry I could not understant your choice") 
        repeat5() 
def repeat5(): 
    rep=int(input("\ndo you want to repeat game ? press 0 for no and 1 for yes ")) 
    if rep==1: 
        guess_the_number() 
    elif rep==0: 
        print("thanks for playing \n") 
        repeat() 
    else: 
        repeat5() 
    
def repeat(): 
    rep=int(input("do you want to play another game ? press 0 for no and 1 for yes ")) 
    if rep==1: 
        select() 
    elif rep==0: 
        print("thanks for playing \n") 
    else: 
        repeat() 

greet() 
