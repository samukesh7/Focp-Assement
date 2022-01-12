print("Stop! Who would cross the Bridge of Death \n"
"Must answer me these questions three, 'ere the other side he see.")

name= input("What is your name? ")
if "arthur" in name or "Arthur" in name: #It checks Arthur in a name.
    print("My liege! You may pass!")
else:
    seek = input("What do you seek?: ")
    if "grail" in seek or "Grail" in seek: #It checks Grail in a seek.
        color = input("What is your favourite color?: ")
        if color[0].lower() == name[0].lower(): #It checks Name and Color 1st character.
            print("You, may Pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")

    else:
        print("Only those who seek the grail may pass.")