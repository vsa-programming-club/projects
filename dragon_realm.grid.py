import random
import time

rooms = [
    "GX DX ",
    " X  G ",
    " XXXXG",
    " D    ",
    ];

room_description = {
    ' ':'an empty passage.',
    'G':'a dull glow.',
    'X':'a wall.',
    'D':'a foul smell.'
    }

movement = {
    "n" : (0,-1),
    "s" : (0,1),
    "e" : (1,0),
    "w" : (-1,0)
    };
gold = 0
strength = 5

def get_room(x,y):
    if x < 0 or y < 0:
        return 'X'
    elif x >= len(rooms[0]) or y >= len(rooms):
        return 'X'
    else:
        return rooms[y][x]
    
def set_room(x,y,char):
    rooms[y] = rooms[y][:x] + char + rooms[y][x+1:]

def print_room(x,y):
    global gold
    #print(x,y)
    if rooms[y][x] == 'D':
        print("There is a dragon in front of you! And he wants to fight!")
    elif rooms[y][x] == ' ':
        print("You are in an empty room.")
    else:
        print("ERROR in program!!!")
    print("To the north, there is",room_description[get_room(x,y-1)])
    print("To the south, there is",room_description[get_room(x,y+1)])
    print("To the east, there is",room_description[get_room(x+1,y)])
    print("To the west, there is",room_description[get_room(x-1,y)])
        
# random start
while True:
    x = random.randint(0,len(rooms[0])-1)
    y = random.randint(0,len(rooms)-1)
    if rooms[y][x] == ' ':
        break

print("""You have entered a strange cave.
All around are dark, musty walls.
Your job is to find 50 pieces of gold and avoid
being killed by dragons.

Good luck!""")

time.sleep(3)

print("And now we begin...")
time.sleep(1)


while gold < 50 and strength > 0:
    print_room(x,y)
    print("You have",gold,"piece(s) of gold and",strength,"unit(s) of strength.")
    print("What would you like to do?")
    action = input()
    if action == '?':
        print("n = go north")
        print("s = go south")
        print("e = go east")
        print("w = go west")
        print("f = fight!")
    elif action == 'f':
        if get_room(x, y) == 'D':
            print("You have",strength,"unit(s) of strength")
            time.sleep(1)
            print("You swing your sword...", end='')
            time.sleep(1)
            if random.randint(0,1) == 0:
                print("and miss")
                time.sleep(1)
                print("The dragon swipes at you...", end='')
                time.sleep(1)
                if random.randint(0,1) == 0:
                    print("and misses")
                else:
                    print("and hits!")
                    time.sleep(1)
                    print("You loose 1 strength point.")
                    strength -= 2
            else:
                print("and hit!")
                time.sleep(1)
                print("The dragon is dead!")
                # and leave some gold!
                set_room(x,y,'G')
        else:
            print("There's no one here to fight.")
    elif action == 'n' or action == 's' or \
         action == 'e' or action == 'w':
        x_inc, y_inc = movement[action]
        if get_room(x+x_inc, y+y_inc) == 'X':
            print("You cannot go in that direction.")
        else:
            x += x_inc
            y += y_inc
    else:
        print("Sorry. I don't know how to do that. Press '?' to learn the commands.")
        
    if rooms[y][x] == 'G':
        print("You have found 10 pieces of gold!")
        time.sleep(1)
        set_room(x,y,' ')
        gold += 10
        print("Now you have",gold,"pieces.")
    print()
     
if strength == 0:
    print("You are dead.")
else:
    print("You have won!")
