try:
    from browser import timer
    from browser import document
    _window = document.getElementById('game')
except:
    pass

from ursina.main import Ursina, application
from ursina import scene



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
color = Empty(red='red', azure='azure', white='white', black='black', clear='rgba(0,0,0,0)', green='green')
from ursina import Sequence, Func, Wait
from ursina.input_handler import held_keys

class Entity:
    def __init__(self, **kwargs):
        self.b = document.createElement("button")
        self.b.style.cssText = '''width:100%; height:100%; position:absolute; top:50%; left:50%; will-change: transform;
        transform:translate(-50%, -50%); font-size:50; color:black; background-size: 100% 100%; padding:0;
        border-radius: 128px; border-style:solid; border-width:0px; border-color: white;'''
        self.enabled = True
        self.parent = scene
        self.x = 0
        self.y = 0
        self.scale_x = 0
        self.scale_y = 0

        self.color = color.white
        for key, value in kwargs.items():
            setattr(self, key ,value)

        scene.entities.append(self)


    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if name == 'x':             self.b.style.left = f'{50+(value*100)}%'
        elif name == 'y':           self.b.style.top = f'{50+(value*100)}%'
        elif name == 'scale_x':     self.b.style.width = f'{value*100}%'
        elif name == 'scale_y':     self.b.style.height = f'{value*100}%'
        elif name == 'origin':      self.b.style.transform = f'translate({(-value[0]-.5)*100}%, {(value[1]-.5)*100}%)'
        # elif name == 'origin_y':    self.b.style.transform = f'translate({(-value-.5)*100}%, -50%)'
        # elif name == 'origin':      self.b.style.transformOrigin = f'{value[0]*100}% {value[0]*100}%'
        # elif name == 'origin':      self.b.style.transformOrigin = f'left center'

        # elif name == 'enabled': self.b.disabled = not value
        elif name == 'visible':     self.b.style.visibility  = ('hidden', 'inherit')[int(value)]
        elif name == 'model':
            if value == None:       self.b.style.backgroundColor = color.clear
            elif value == 'quad':   self.b.style.borderRadius = '0%'

        # if name == 'text': self.b.style.innerHTML = value
        elif name == 'update':
            if callable(value): timer.set_interval(value, 60)
            else:               timer.clear_interval(update)

        elif name == 'parent':      value.b.appendChild(self.b)
        elif name == 'color':       self.b.style.backgroundColor = value
        elif name == 'texture':     self.b.style.backgroundImage = f"url('{value}.jpg'), url('{value}.png')"



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
b = Button()
b.scale_x = .5
b.scale_y = .5
# b.model = None
# # b.origin_x = -.5
# b.x = 0

# e = Entity()

c = Button(parent=b, scale_x=.5, scale_y=1, x=0, y=0, color=color.green,
    origin=(-.5,0),
    model='quad', text='test\nf e f k fwfwefwefwef\nfewij', background_color=color.red,
    # texture='shore'
    )

# c.text_entity.b.style.margin = '50% 0 0 0'
# c.text_entity.origin = (-.5, 0)
# c.text_entity.origin = (0, 0)
c.text_entity.origin = (.5, .5)
# c.text_entity.b.styletransform:translate(-50%, -50%)
# c.text_entity.b.style.textAlign = 'left'
# c.text_entity.x = .5
# print(c.text_entity.x)
# b.x += .25
print(c.x)

# b.
# print(b)
# def update():
#     print('lol', held_keys['d'])
#
#     b.x += held_keys['d'] * 1
#     b.x -= held_keys['a'] * 1

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

# def _update_wrapper(i):
#     # global id
#     timer.request_animation_frame(_update_wrapper)
#     if update:
#         update()
# _update_wrapper(0)



def invoke(func, *args, **kwargs):
    if delay == 0:
        func(*args, **kwargs)
        return

    timer.set_timeout(func, *args, **kwargs, delay=delay*1000)
