from ursina import *



app = Ursina()


# Button = Entity
# b = Entity()
# b.scale_x = .5
# b.scale_y = .5
# b.model = None
# # b.origin_x = -.5
# b.x = 0

# e = Entity()

# c = Button(parent=b, scale_x=.5, scale_y=1, x=0, y=0, color=color.green,
#     origin=(-.5,0),
#     model='quad', text='test\nf e f k fwfwefwefwef\nfewij', background_color=color.red,
#     # texture='shore'
#     )
#
# # c.text_entity.b.style.margin = '50% 0 0 0'
# # c.text_entity.origin = (-.5, 0)
# # c.text_entity.origin = (0, 0)
# c.text_entity.origin = (.5, .5)
# # c.text_entity.b.styletransform:translate(-50%, -50%)
# # c.text_entity.b.style.textAlign = 'left'
# # c.text_entity.x = .5
# # print(c.text_entity.x)
# # b.x += .25
# print(c.x)

# def update():
#     # print('lol', held_keys['d'])
#
#     b.x += held_keys['d'] * .01
#     b.x -= held_keys['a'] * .01

# def entity_update():
#     print('a')
#     c.x += .5
# c.update = entity_update
#
# def entity_input(key):
#     if key == 'a':
#         c.x -= 1
# #
# c.input = entity_input
# def test():
#     print('ddddddddddddddddddddd')
#
# c.on_click = Func(print, 'yolo')

# def input(key):
#     print('.-........', key)





# from ursina import *


# app = Ursina()

# Entity()

# def input(key):
#     if key == '-':
#         scene.scale_x *= .9
#         scene.scale_y *= .9
#     if key == '+':
#         scene.scale_x /= .9
#         scene.scale_y /= .9
#
#     if key == 'd':
#         camera.x += .1

camera.fov = 4
camera.position = (1, 1)
# Text.default_resolution *= 2


player = Entity(name='o', color=color.azure)
cursor = Tooltip(player.name, color=player.color, origin=(0,0), scale=4, enabled=True)
cursor.background.color = color.clear
bg = Entity(parent=scene, model='quad', texture='shore', scale=(16,8), z=10, color=color.light_gray)
mouse.visible = False

# create a matrix to store the buttons in. makes it easier to check for victory
board = [[None for x in range(3)] for y in range(3)]

for y in range(3):
    for x in range(3):
        b = Button(parent=scene, position=(x,y))
        board[x][y] = b

        def on_click(b=b):
            b.text = player.name
            b.color = player.color
            b.collision = False
            check_for_victory()

            if player.name == 'o':
                player.name = 'x'
                player.color = color.orange
            else:
                player.name = 'o'
                player.color = color.azure

            # cursor.text = player.name

        b.on_click = on_click


def check_for_victory():
    name = player.name

    won = (
    (board[0][0].text == name and board[1][0].text == name and board[2][0].text == name) or # across the bottom
    (board[0][1].text == name and board[1][1].text == name and board[2][1].text == name) or # across the middle
    (board[0][2].text == name and board[1][2].text == name and board[2][2].text == name) or # across the top
    (board[0][0].text == name and board[0][1].text == name and board[0][2].text == name) or # down the left side
    (board[1][0].text == name and board[1][1].text == name and board[1][2].text == name) or # down the middle
    (board[2][0].text == name and board[2][1].text == name and board[2][2].text == name) or # down the right side
    (board[0][0].text == name and board[1][1].text == name and board[2][2].text == name) or # diagonal /
    (board[0][2].text == name and board[1][1].text == name and board[2][0].text == name))   # diagonal \

    if won:
        print('winner is:', name)
        destroy(cursor)
        # del cursor
        mouse.visible = True
        Panel(z=1, scale=10, model='quad')
        t = Text(f'player\n{name}\nwon!', scale=3, origin=(0,0), background=True)
        # t.create_background(padding=(.5,.25), radius=Text.size/2)
        # t.background.color = player.color.tint(-.2)


Text('test text')

app.run()
