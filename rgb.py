def formula(rgb):
    if rgb < 0:
        return 0
    if rgb > 255:
        return 255
    return rgb

def rgb(r, g, b): #0<=rgb<=255
    return "{:02X}{:02X}{:02X}".format(formula(r), formula(g), formula(b)) #Formato hexadecimal
