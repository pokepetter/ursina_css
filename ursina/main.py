import __main__
from browser import document
from browser import timer
_window = document.getElementById('game')
from ursina import input_handler
# from ursina import application
class Empty:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key ,value)

application = Empty()
application.paused = False
application.time_scale = 1
application.sequences = list()
application.trace_entity_definition = False # enable to set entity.line_definition
application.print_entity_definition = False
application.package_folder = ''
application.asset_folder = ''
application.development_mode = True

class Window():
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        _window.style.width = f'{value[0]}px'
        _window.style.heigth = f'{value[1]}px'
        self.aspect_ratio = value[0] / value[1]

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        _window.style.backgroundColor = value


window = Window()
window.color = 'gray'
window.size = (1920, 1080)


from ursina import Entity
scene = Entity(model=None, scale_x=1/window.aspect_ratio)
scene.entities = list()
# scene.b = document.createElement("div")
# scene.b.style.cssText = '''width:56.25%; height:100%; position:absolute; top:50%; left:50%;
# transform:translate(-50%, -50%); color:white; background-color:clear;'''
_window.appendChild(scene.b)


class Ursina:
    def __init__(self):
        self._input_name_changes = {
            'arrowup' : 'arrow up',
            'arrowright' : 'arrow right',
            'arrowdown' : 'arrow down',
            'arrowleft' : 'arrow left',
            ' ' : 'space',
            '!':'1', '@':'2', '#':'3', '$':'4', '%':'5', '^':'6', '&':'7', '*':'8', '(':'9', ')':'0',
                     '"':'2',          '¤':'4',          '&':'6', '/':'7', '(':'8', ')':'9', '=':'0',
        }

        document.addEventListener('keydown', self.input)
        document.addEventListener('keyup', self.input_up)


    def input_up(self, key):
        if not isinstance(key, str):
            if key.repeat:
                return
            key = key.key

        if key in  ('wheel_up', 'wheel_down'):
            return

        key += ' up'
        self.input(key)


    def input_hold(self, key):
        if key in self._input_name_changes:
            key = self._input_name_changes[key]

        key += ' hold'
        self.input(key)


    def input(self, key):
        if not isinstance(key, str):
            if key.repeat:
                self.input_hold(key.key)
                return
            key = key.key


        # print('------------', key)
        key = key.lower()
        if key in self._input_name_changes:
            key = self._input_name_changes[key]

        key = key.replace('control-', '')
        key = key.replace('shift-', '')
        key = key.replace('alt-', '')

        if key in input_handler.rebinds:
            key = input_handler.rebinds[key]

        try: input_handler.input(key)
        except: pass
        if not application.paused:
            if hasattr(__main__, 'input'):
                __main__.input(key)


        for entity in scene.entities:
            if entity.enabled:
                if hasattr(entity, 'input'):
                    entity.input(key)

                if hasattr(entity, 'scripts'):
                    for script in entity.scripts:
                        if hasattr(script, 'input'):
                            script.input(key)



    def run(self):
        def _update_wrapper(i):
            # global id
            timer.request_animation_frame(_update_wrapper)
            if hasattr(__main__, 'update'):
                __main__.update()
        _update_wrapper(0)
        # pass
