from ursina import *


class Text(Entity):

    size = .025
    default_font = 'OpenSans-Regular.ttf'
    default_resolution = 1080 * size * 2
    start_tag = '<'
    end_tag = '>'


    def __init__(self, text='', **kwargs):
        super().__init__()
        self.name = 'text_entity'
        self.parent = camera.ui
        self.background_color = color.clear
        self.color = color.smoke
        self.b.style.whiteSpace = 'pre'
        self.b.style.overflow = 'visible'
        self.b.style.verticalAlign = 'text-top'
        self.b.style.pointerEvents = 'none'
        self.origin = (0,0)
        self._background = None
        self.text = text

        self.width = 0
        self.height = 0

        for key, value in kwargs.items():
            setattr(self, key ,value)


    def __setattr__(self, name, value):
        if name == 'text':                  self.b.innerHTML = value
        elif name == 'color':               self.b.style.color = value
        elif name == 'background_color':    self.b.style.backgroundColor = value
        elif name == 'scale':               self.b.style.fontSize = f'{50*value}px'
        elif name == 'origin':
            self.b.style.textAlign = ('left', 'center', 'right')[int((value[0]*2)+1)]
            self.b.style.direction = ('ltr', 'rtl', 'rtl')[int((value[0]*2)+1)]
            #
            # self.b.style.textAlign = ('text-top', 'middle', 'text-bot')[int((value[0]*2)+1)]
            # self.b.style.transformOrigin = f'{value} {}'
        else:                               super().__setattr__(name, value)

    def create_background(self, padding=size*2, radius=size, color=color.black66):
        from ursina import Quad, destroy

        if self._background:
            destroy(self._background)

        self._background = Entity(parent=self, z=1)

        if isinstance(padding, (int, float, complex)):
            padding = (padding, padding)

        w, h = self.width + padding[0], self.height + padding[1]
        # self._background.x -= self.origin_x * self.width
        # self._background.y -= self.origin_y * self.height

        self._background.model = Quad(radius=radius, scale=(w/self.scale_x, h/self.scale_y))
        self._background.color = color


    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        if value == True:
            self.create_background()
        elif self._background:
            destroy(self._background)



class Tooltip(Text):
    def __init__(self, text='', **kwargs):
        super().__init__(text, **kwargs)
        self.name = 'tooltip'
        self.background = Entity(parent=self, model='quad')
        # self.create_background()

    def update(self):
        # print('lol', mouse.position)
        self.position = mouse.position
