import __main__
from browser import document
from browser import timer
import browser
_window = document.getElementById('game')
from ursina import input_handler
from ursina import color
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
    def __init__(self, **kwargs):
        self.b = _window

        self.size = (self.b.width, self.b.height)
        self.color = color.gray


    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

        if name == 'width':             self.b.style.width = f'{value}px'
        if name == 'heigth':            self.b.style.heigth = f'{value}px'
        if name == 'size':              self.width, self.height = value[0], value[1]

        if name == 'color':             self.b.style.backgroundColor = value


    @property
    def aspect_ratio(self):
        return self.width / self.height

    @property
    def position(self):
        r = self.b.getBoundingClientRect()
        return (r.left, r.top)


    @property
    def top(self): return (0, .5)
    @property
    def bottom(self): return (0, -.5)
    @property
    def right(self): return (.5, 0)
    @property
    def left(self): return (-.5, 0)


    @property
    def bottom_left(self): return (-.5 * self.aspect_ratio, -.5)
    @property
    def top_left(self): return (-.5 * self.aspect_ratio, .5)
    @property
    def bottom_right(self): return (.5 * self.aspect_ratio, -.5)
    @property
    def top_right(self): return (.5 * self.aspect_ratio, .5)



window = Window()


from ursina import Entity
scene = Entity(model=None, scale_x=1/window.aspect_ratio, name='scene', entities=[])
_window.appendChild(scene.b)

# mouse = Empty()

from ursina.camera import Camera
camera = Camera()
class Mouse():
    def __init__(self):
        self.enabled = True
        # self.locked = False
        self.position = (0,0)
        self.delta = (0,0)
        self.prev_x = 0
        self.prev_y = 0
        self.velocity = (0,0)
        self.prev_click_time = time.time()
        self.double_click_distance = .5

        self.hovered_entity = None
        self.left = False
        self.right = False
        self.middle = False
        self.delta_drag = (0,0)

        self.i = 0
        self.update_rate = 10
        # self._mouse_event = None


    def input(self, key):
        if not self.enabled:
            return

        if key.endswith('mouse down'):
            self.start_x = self.x
            self.start_y = self.y

        elif key.endswith('mouse up'):
            self.delta_drag = (
                self.x - self.start_x,
                self.y - self.start_y
                )


        if key == 'left mouse down':
            self.left = True
            if self.hovered_entity:
                if hasattr(self.hovered_entity, 'on_click'):
                    self.hovered_entity.on_click()
                for s in self.hovered_entity.scripts:
                    if hasattr(s, 'on_click'):
                        s.on_click()
                    # try:
                        # s.on_click()
                    # except:
                    #     pass
            # double click
            if time.time() - self.prev_click_time <= self.double_click_distance:
                ursina.main.input('double click')
            self.prev_click_time = time.time()


        if key == 'left mouse up':
            self.left = False
        if key == 'right mouse down':
            self.right = True
        if key == 'right mouse up':
            self.right = False
        if key == 'middle mouse down':
            self.middle = True
        if key == 'middle mouse up':
            self.middle = False


    def update(self):
        if not self.enabled or not hasattr(self, '_mouse_event'):
            self.velocity = (0,0)
            self.moving = False
            return

        event = self._mouse_event

        self.x = min(max((event.x-window.position[0]-(window.size[0]/2))/window.size[0]*window.aspect_ratio, -window.aspect_ratio/2,), window.aspect_ratio/2)
        self.y = min(max(((-event.y+window.position[1])/window.size[1]) +.5, -.5), .5)

        self.position = (self.x, self.y)
        self.moving = self.x + self.y != self.prev_x + self.prev_y

        if self.moving:
            # if self.locked:
            #     self.velocity = self.position
            #     application.base.win.move_pointer(0, int(window.size[0] / 2), int(window.size[1] / 2))
            # else:
            self.velocity = (self.x - self.prev_x, (self.y - self.prev_y) / window.aspect_ratio)
        else:
            self.velocity = (0,0)

        if self.left or self.right or self.middle:
            self.delta = (self.x - self.start_x, self.y - self.start_y)

        self.prev_x = self.x
        self.prev_y = self.y


        self.i += 1
        if self.i < self.update_rate:
            return

        self.i = 0

        self.hits = [e.entity for e in document.elementsFromPoint(event.x, event.y) if hasattr(e, 'entity')]

        if not self.hits:
            self.hovered_entity = None

        else:
            self.hovered_entity = self.hits[0]

            if not self.hovered_entity.hovered:
                self.hovered_entity.hovered = True
                if hasattr(self.hovered_entity, 'on_mouse_enter'):
                    self.hovered_entity.on_mouse_enter()

        self.unhover_everything_not_hit()


    def unhover_everything_not_hit(self):
        for e in scene.entities:
            if e == self.hovered_entity:
                continue

            if e.hovered:
                e.hovered = False
                if hasattr(e, 'on_mouse_exit'):
                    e.on_mouse_exit()


import time
mouse = Mouse()


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


        # # from ursina.mouse import mouse
        self.mouse_down_names = ('left mouse down', 'middle mouse down', 'right mouse down')
        self.mouse_up_names = ('left mouse up', 'middle mouse up', 'right mouse up')

        def _mousedown(event):
            i = min(event.which-1, 3)
            self.input(self.mouse_down_names[i])
        def _mouseup(event):
            i = min(event.which-1, 3)
            self.input(self.mouse_up_names[i])
        def _mousescroll(event):
            self.input('scroll down' if event.deltaY > 0 else 'scoll up')
        def _mousemove(event):
            # mouse.update(event)
            mouse._mouse_event = event

        document.addEventListener('mousedown', _mousedown)
        document.addEventListener("mouseup", _mouseup)
        document.addEventListener("wheel", _mousescroll)
        document.addEventListener("mousemove", _mousemove)



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
            timer.request_animation_frame(_update_wrapper)

            # time between frames
            dt = 1/60 * application.time_scale
            time.dt = dt

            mouse.update()

            if hasattr(__main__, 'update') and not application.paused:
                __main__.update()

            for seq in application.sequences:
                seq.update()

            for entity in scene.entities:
                if entity.enabled == False or entity.ignore:
                    continue

                if application.paused and entity.ignore_paused == False:
                    continue

                if hasattr(entity, 'update'):
                    entity.update()


                if hasattr(entity, 'scripts'):
                    for script in entity.scripts:
                        if script.enabled and hasattr(script, 'update'):
                            script.update()

        _update_wrapper(0)

        loading_text = document.getElementById('loading_text');
        loading_text.remove();
        # pass



def invoke(func, *args, **kwargs):
    if delay == 0:
        func(*args, **kwargs)
        return

    timer.set_timeout(func, *args, **kwargs, delay=delay*1000)



def destroy(entity, delay=0):
    if delay == 0:
        _destroy(entity)
        return

    s = Sequence(
        Wait(delay),
        Func(_destroy, entity)
    )
    s.start()


def _destroy(entity):
    if not entity:
        print('entity is None')
        return
    if entity in scene.entities:
        scene.entities.remove(entity)

    if hasattr(entity, 'on_destroy'):
        entity.on_destroy()

    if hasattr(entity, 'scripts'):
        for s in entity.scripts:
            del s

    if hasattr(entity, 'animations'):
        for anim in entity.animations:
            anim.finish()
            anim.kill()

    if hasattr(entity, 'tooltip'):
        destroy(entity.tooltip)
        # entity.tooltip.removeNode()
    if hasattr(entity, '_on_click') and isinstance(entity._on_click, Sequence):
        entity._on_click.kill()


    entity.b.remove()

    #unload texture
    # if hasattr(entity, 'texture') and entity.texture != None:
    #     entity.texture.releaseAll()

    del entity
