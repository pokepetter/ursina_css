from browser import document
_window = document.getElementById('game')
from ursina import color



class Entity:
    def __init__(self, **kwargs):
        self.b = document.createElement("button")
        self.b.style.cssText = '''width:100%; height:100%; position:absolute; top:50%; left:50%; will-change: transform;
        transform:translate(-50%, -50%); font-size:50; color:black; background-size: 100% 100%; padding:0;
        border-radius: 128px; border-style:solid; border-width:0px; border-color: white;'''
        self.enabled = True
        try:
            from ursina.main import scene
            self.parent = scene
            scene.entities.append(self)
        except:
            print('no scene entity yet')
        self.x = 0
        self.y = 0
        self.scale_x = 1
        self.scale_y = 1
        self.color = color.white
        self.model = None

        for key, value in kwargs.items():
            setattr(self, key ,value)



    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if name == 'x':             self.b.style.left = f'{50+(value*100)}%'
        elif name == 'y':           self.b.style.top = f'{50+(-value*100)}%'
        elif name == 'z':           self.b.style.zIndex = -value

        elif name == 'position':
            self.x = value[0]
            self.y = value[1]
            if len(value)==3:
                self.z=value[2]

        elif name == 'scale_x':     self.b.style.width = f'{value*100}%'
        elif name == 'scale_y':     self.b.style.height = f'{value*100}%'
        elif name == 'scale':       self.scale_x = value[0]; self.scale_y = value[1]

        elif name == 'origin':      self.b.style.transform = f'translate({(-value[0]-.5)*100}%, {(value[1]-.5)*100}%)'
        elif name == 'origin_x':    self.origin = (value, self.origin[1])
        elif name == 'origin_y':    self.origin = (self.origin[0], value)

        # elif name == 'ignore':
        #     if self.update

        elif name == 'enabled':     self.visible = value
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