
def color(h, s, v, a=1):
    l = (2 - s) * v / 2

    if l != 0:
        if l == 1:
            s = 0
        elif l < 0.5:
            s = s * v / (l * 2)
        else:
            s = s * v / (2 - l * 2)

    return f'hsla({h}, {s*100}%, {l*100}%, {a})'

hsv = color


white =         color(0, 0, 1)
smoke =         color(0, 0, 0.96)
light_gray =    color(0, 0, 0.75)
gray =          color(0, 0, 0.5)
dark_gray =     color(0, 0, 0.25)
black =         color(0, 0, 0)
red =           color(0, 1, 1)
orange =        color(30, 1, 1)
yellow =        color(60, 1, 1)
lime =          color(90, 1, 1)
green =         color(120, 1, 1)
turquoise =     color(150, 1, 1)
cyan =          color(180, 1, 1)
azure =         color(210, 1, 1)
blue =          color(240, 1, 1)
violet =        color(270, 1, 1)
magenta =       color(300, 1, 1)
pink =          color(330, 1, 1)

clear = color(0, 0, 0, 0)
white10 = color(1,1,1, 0.10)
white33 = color(1,1,1, 0.33)
white50 = color(1,1,1, 0.50)
white66 = color(1,1,1, 0.66)
black10 = color(0,0,0, 0.10)
black33 = color(0,0,0, 0.33)
black50 = color(0,0,0, 0.50)
black66 = color(0,0,0, 0.66)
