def alphabet_war(fight):
    dcha = 0
    izq = 0
    for lucha in fight:
        if lucha =="m":
            dcha+=4
        elif lucha =="q":
            dcha+=3
        elif lucha == "d":
            dcha+=2
        elif lucha == "z":
            dcha+=1
        elif lucha =="w":
            izq+=4
        elif lucha =="p":
            izq+=3
        elif lucha =="b":
            izq+=2
        elif lucha =="s":
            izq+=1
    if dcha>izq:
        return("Right side wins!")
    elif dcha <izq:
        return("Left side wins!")
    elif dcha == izq:
        return("Let's fight again!")
