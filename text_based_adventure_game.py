from sys import exit

def start_room():
    print "The last thing you remember is the blaring of car horns and bright lights through your cars front windshield, your wife screaming beside you, then a sear of pain and a blinding flash of light. Then silence. You now find yourself in a dank chamber, lit only by the dim glimmer of candles, and only two doors, on your left and on your right. A robed man stands beside you.\n\"Welcome,\" he says, \"to the void before the beyond. Your journey is almost complete, but first you must prove yourself worthy.\"\n The man then walks through the door to your left."
    print "Do you follow him, or take the door to your right?"
    
    next = raw_input("> ")
    
    if "follow" in next:
        left_room()
    elif "right" in next:
        right_room()
    else :
        print "I didn't get that. Did you want to follow or take the door to your right?"
        start_room()

def left_room():
    print "You walk through a dark and twisty hallway and eventually feel your way to another dim room, this time with two doors. The first leads to another dark hallway. The second takes up an entire wall. It is carved ornately and covered with gold leaf. You open it up and see nothing but and endless field of dazzling light behind it."
    print "Do you enter the door to heaven? Or do you continue on your journey through the other door?"
    
    next = raw_input("> ")
    
    if "heaven" in next:
        hell("You enter the door to heaven and immediately feel encompassed by the warm light. However, just as quickly, you feel the warmth turn to heat and then searing pain. You feel a sinking in your stomach as you realize you have chosen the wrong door. The robed man approaches you once more; he is holding an axe and he is smiling.")
    elif "continue" in next:
        courtyard()
    else :
        print "I didn't get that. If you want to go through the door to heaven, type \"heaven\", if you want to continue, type \"continue\"."
        left_room()

def right_room():
    print "You find yourself in a room with another door and a beatiful woman. She is beckoning you to come closer, but says not a word."
    print "Do you go over to the woman, or continue your journey through the door?"
    
    next = raw_input("> ")
    
    if "woman" in next:
        hell("You go over to the woman. She smiles and embraces you, and for an instant, you feel safe. Then, you feel a stinging pain in your neck, and the room disappears around you. The robed man appears from behind the woman, and this time he is carrying a nine tailed whip. He is smiling like the devil.")
    elif "continue" in next:
        courtyard()
    else :
        print "I didn't get that. Type \"woman\" if you want to go to the beautiful woman. Type \"continue\" if you want to continue your journey."
        right_room()

def courtyard():
    print "At the end of a long hallway, you wind yourself in an open-air courtyard, only the sky looks different than any sky you've ever seen. It is pure white and looks strangely flat. A gargoyle winks at you and says, \"you've passed the first test. Only one more to go.\" You exit the courtyard and continue down the next hallway."
    sphinx()

def sphinx():
    print "You almost get lost in the twisting passages, but eventually you feel your way through the pitch darkness to a small room with nothing but a torch and a statue of a sphinx inside of it. The sphinx opens its eyes and speaks. \"A riddle for thee. What animal walks on four legs at morning, on two legs at noon, and three legs at night?\""
    
    next = raw_input("> ")
    
    if "man" in next:
        the_beyond()
    else :
        hell("The sphinx bears its teeth. \"You have chosen unwisely\" it roars, and bats your face with its claws. You find your vision fading, and yourself lying on the floor. The last thing you see is the robed man, peering down at you and grinning.")

def the_beyond():
    print "The sphinx smiles warmly and says, \"He is indeed. Go in peace.\" His tail moves out of the way of the final door, and you are allowed to pass though it. In the beyond you are eneveloped in a comforting gray cloud, and for a moment you wonder if you made the right choice after all--then, out of the fog, your wife approaches you and wraps you in an embrace. Behind her you see your parents, and your grandparents, and your brother who you haven't seen since you were fourteen years old. You smile and you know that you are home."
    exit(0)

def hell(why):
    print why
    exit(0)

start_room()
