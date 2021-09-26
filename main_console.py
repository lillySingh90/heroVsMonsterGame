import threading
import time

# global variables
hero_health = 40
orc_health = 7
dragon_health = 20


def thread_orc():
    global hero_health
    global orc_health
    while orc_health > 0 and hero_health > 0:
        time.sleep(1.5)
        hero_health = hero_health - 1
        print("Orc attacked... Hero health: ", hero_health)


def thread_dragon():
    global hero_health
    global dragon_health
    while dragon_health > 0 and hero_health > 0:
        time.sleep(2.0)
        hero_health = hero_health - 3
        print("Dragon attacked... Hero health: ", hero_health)


# making threads for orc and dragon
orc = threading.Thread(target=thread_orc)
dragon = threading.Thread(target=thread_dragon)

# to start the thread
orc.start()
dragon.start()

# main user loop
while hero_health > 0 and orc_health > 0 and dragon_health > 0:
    var = input("attack ")
    if var == "orc":
        orc_health = orc_health - 2
        print("Hero attack Orc ... Orc health is ", str(orc_health))
    elif var == "dragon":
        dragon_health = dragon_health - 2
        print("Hero attack dragon ... Dragon health is ", str(dragon_health))

# Wait for threads to finish
orc.join()
dragon.join()
























