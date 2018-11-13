import time

def displayIntro():
    print('''You are in a land full of dragons. Your job
is to find the treasure before you are killed by one
of these terrifying beasts.''')

done = False

def printCave(chosenCave):
    global done
    print()
    if caveNumber == 1:
        print('''You are in a large cave.
There is a narrow passage to the left and a wide passage to the right.
Enter 1 to go left and 2 to go right.''')
        choice = [2, 5]
    elif caveNumber == 2:
        print('''The narrow passage has led to a long stairs.
At the top of the stairs is a strange light.
Enter 1 to go up the stairs or 2 to turn back.''')
        choice = [3, 1]
    elif caveNumber == 3:
        print('''You are at the top of the stairs.
In front of you is pile of dead men's bones.
Ahead of you is a small lake.
Enter 1 to go to the lake or 2 to go back down the stairs.''')
        choice = [4, 2]
    elif caveNumber == 4:
        print('''The lake is very large and there is no
way across. Enter 1 to turn back.''')
        choice = [3]
    elif caveNumber == 5:
        print('''The wide passage opens to a broad field.
Across the field is a stream. There is also a grove of trees.
Enter 1 to go to the stream, 2 to go to the grove of trees,
or 3 to re-enter the cave.''')
        choice = [6,7,1]
    elif caveNumber == 6:
        print('''By the stream there is a massive dragon.''')
        time.sleep(1)
        print('He breathes out a stream of fire...')
        time.sleep(1)
        print('And you die. You lose!')
        done = True
    elif caveNumber == 7:
        print('''In the grove of trees you find a small chest.''')
        time.sleep(1)
        print('You open the chest...')
        time.sleep(1)
        print('And find a massive hoard of treasure! You win!')
        done = True
    else:
        print('''You have fallen off the edge of the world.
I guess the programmer must do more work.
Enter 1 to return to the cave''')
        choice = [1]

    print()
    if done:
        return
    while True:
        n = int(input("Your choice:"))
        if n == 0 or n > len(choice):
            print("That is not a valid choice here.")
        else:
            break
    return choice[n-1]

displayIntro()
caveNumber = 1
while not done:
    caveNumber = printCave(caveNumber)

print('Press ENTER to exit')
input()

