from ursina.main import Ursina, application


class Empty:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key ,value)

# class Text(Entity):
#     def __setattr__(self, name, value):
#         object.__setattr__(self, name, value)
#         if name == 'color': self.parent.b.style.color = value
#         if name == 'text': self.parent.b.


app = Ursina()
camera = Empty(x=0, y=0)
camera.ui = Empty(x=0, y=0)
Quad = Empty
Circle = Empty

from ursina import *

class Text(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.background_color = color.clear
        self.scale_x = 1
        self.scale_y = 1
        self.color = color.black
        self.b.style.whiteSpace = 'pre'
        self.b.style.overflow = 'visible'
        self.b.style.verticalAlign = 'text-top'


        for key, value in kwargs.items():
            setattr(self, key ,value)

    def __setattr__(self, name, value):
        if name == 'text':                  self.parent.b.innerHTML = value
        elif name == 'color':               self.b.style.color = value
        elif name == 'background_color':    self.b.style.backgroundColor = value
        elif name == 'scale':               self.b.style.fontSize = value
        elif name == 'origin':
            self.b.style.textAlign = ('left', 'center', 'right')[int((value[0]*2)+1)]
            self.b.style.direction = ('ltr', 'rtl', 'rtl')[int((value[0]*2)+1)]
            #
            # self.b.style.textAlign = ('text-top', 'middle', 'text-bot')[int((value[0]*2)+1)]
            # self.b.style.transformOrigin = f'{value} {}'
        else:                               super().__setattr__(name, value)


class Button(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.text_entity = Text(parent=self)
        self.model = 'quad'
        self.color = 'rgba(0,0,0,0.66)'
        for key, value in kwargs.items():
            setattr(self, key ,value)


    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name == 'text':  self.text_entity.b.innerHTML = value

    @property
    def on_click(self):
        return self._on_click

    @on_click.setter
    def on_click(self, value):
        self._on_click = value
        self.b.onclick = self._click_callback

    def _click_callback(self, ev):
        if hasattr(self, '_on_click'):
            self._on_click()




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





def invoke(func, *args, **kwargs):
    if delay == 0:
        func(*args, **kwargs)
        return

    timer.set_timeout(func, *args, **kwargs, delay=delay*1000)



class Camera(Entity):
    def __init__(self):
        super().__init__()
        self.orthographic = True
        self.fov = 1


    @property
    def fov(self):
        try:
            return self._fov
        except:
            print('error')
            return 1

    @fov.setter
    def fov(self, value):
        self._fov = value
        scene.scale = (1/value/window.aspect_ratio, 1/value)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        scene.position = (-value[0] / self.fov / window.aspect_ratio, -value[1] / self.fov)


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        scene.x = -value / self.fov / window.aspect_ratio


    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._y = value
        scene.y = -value / self.fov

camera = Camera()

from ursina import *


app = Ursina()

Entity()

def input(key):
    if key == '-':
        scene.scale_x *= .9
        scene.scale_y *= .9
    if key == '+':
        scene.scale_x /= .9
        scene.scale_y /= .9

    if key == 'd':
        camera.x += .1

camera.fov = 4
camera.position = (1, 1)
# Text.default_resolution *= 2

# for y in range(3):
#     for x in range(3):
#         b = Button(parent=scene, position=(x,y))

# create a matrix of buttons
# Button(model='quad')
board = [[Button(parent=scene, model='quad', position=(x,y)) for x in range(3)] for y in range(3)]
#
player_name = 'o'
player_color = color.azure
# cursor = Tooltip(player_name, color=player_color, origin=(0,0), scale=4, enabled=True)
# cursor.background.color = color.clear
bg = Entity(parent=scene, model='quad', texture='shore', scale=(16,8), z=10, color=color.white)
# mouse.visible = False


def input(key):
    global player_name, player_color, cursor

#     if key == 'left mouse down' and mouse.hovered_entity:
#         b = mouse.hovered_entity
#         b.text = player_name
#         b.color = player_color
#         b.collision = False
#         check_for_victory()
#
#         if player_name == 'o':
#             player_name = 'x'
#             player_color = color.orange
#         else:
#             player_name = 'o'
#             player_color = color.azure
#
#         cursor.text = player_name
#
#
# def check_for_victory():
#     global board, cursor, player_name, player_color
#     name = player_name
#
#     won = (
#     (board[0][0].text == name and board[1][0].text == name and board[2][0].text == name) or # across the bottom
#     (board[0][1].text == name and board[1][1].text == name and board[2][1].text == name) or # across the middle
#     (board[0][2].text == name and board[1][2].text == name and board[2][2].text == name) or # across the top
#     (board[0][0].text == name and board[0][1].text == name and board[0][2].text == name) or # down the left side
#     (board[1][0].text == name and board[1][1].text == name and board[1][2].text == name) or # down the middle
#     (board[2][0].text == name and board[2][1].text == name and board[2][2].text == name) or # down the right side
#     (board[0][0].text == name and board[1][1].text == name and board[2][2].text == name) or # diagonal /
#     (board[0][2].text == name and board[1][1].text == name and board[2][0].text == name))   # diagonal \
#
#     if won:
#         print('winner is:', name)
#         destroy(cursor)
#         mouse.visible = True
#         Panel(z=1, scale=10, model='quad')
#         t = Text('player\n'+name+'\nwon!', scale=3, origin=(0,0), background=True)
#         t.create_background(padding=(.5,.25), radius=Text.size/2)
#         t.background.color = player_color.tint(-.2)


app.run()
