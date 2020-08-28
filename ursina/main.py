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
window.position=(0,0)


from ursina import Entity
scene = Entity(model=None, scale_x=1/window.aspect_ratio, name='scene')

scene.entities = list()
# scene.b = document.createElement("div")
# scene.b.style.cssText = '''width:56.25%; height:100%; position:absolute; top:50%; left:50%;
# transform:translate(-50%, -50%); color:white; background-color:clear;'''
_window.appendChild(scene.b)

mouse = Empty()

from ursina.camera import Camera
camera = Camera()
# class Mouse():
#     def __init__(self):
#         self.enabled = True
#         # self.locked = False
#         self.position = (0,0)
#         self.delta = (0,0)
#         self.prev_x = 0
#         self.prev_y = 0
#         self.velocity = (0,0)
#         self.prev_click_time = time.time()
#         self.double_click_distance = .5
#
#         self.hovered_entity = None
#         self.left = False
#         self.right = False
#         self.middle = False
#         self.delta_drag = (0,0)
#
#         self.i = 0
#         self.update_rate = 10
#         self._mouse_event = None
#
#
#     @property
#     def x(self):
#         return self.position[0]
#     @property
#     def y(self):
#         return self.position[1]
#
#
#     def input(self, key):
#         if not self.enabled:
#             return
#
#         if key.endswith('mouse down'):
#             self.start_x = self.x
#             self.start_y = self.y
#
#         elif key.endswith('mouse up'):
#             self.delta_drag = (
#                 self.x - self.start_x,
#                 self.y - self.start_y
#                 )
#
#
#         if key == 'left mouse down':
#             self.left = True
#             if self.hovered_entity:
#                 if hasattr(self.hovered_entity, 'on_click'):
#                     self.hovered_entity.on_click()
#                 for s in self.hovered_entity.scripts:
#                     if hasattr(s, 'on_click'):
#                         s.on_click()
#                     # try:
#                         # s.on_click()
#                     # except:
#                     #     pass
#             # double click
#             if time.time() - self.prev_click_time <= self.double_click_distance:
#                 ursina.main.input('double click')
#             self.prev_click_time = time.time()
#
#
#         if key == 'left mouse up':
#             self.left = False
#         if key == 'right mouse down':
#             self.right = True
#         if key == 'right mouse up':
#             self.right = False
#         if key == 'middle mouse down':
#             self.middle = True
#         if key == 'middle mouse up':
#             self.middle = False
#
#
#     def update(self):
#         if not self.enabled:
#             self.velocity = (0,0)
#             return
#
#         # self.position = (self.x, self.y)
#         self.moving = self.x + self.y != self.prev_x + self.prev_y
#
#         if self.moving:
#             # if self.locked:
#             #     self.velocity = self.position
#             #     application.base.win.move_pointer(0, int(window.size[0] / 2), int(window.size[1] / 2))
#             # else:
#             self.velocity = (self.x - self.prev_x, (self.y - self.prev_y) / window.aspect_ratio, 2)
#         else:
#             self.velocity = (0,0)
#
#         if self.left or self.right or self.middle:
#             self.delta = (self.x - self.start_x, self.y - self.start_y)
#
#         self.prev_x = self.x
#         self.prev_y = self.y
#
#
#         self.i += 1
#         if self.i < self.update_rate:
#             return
#
#         self.i = 0
#         # try:
#             # self.hovered_entity = document.elementFromPoint(self._mouse_event.x, self._mouse_event.y).entity
#         self.hits = document.elementsFromPoint(self._mouse_event.x, self._mouse_event.y)
#         if not self.hits:
#             print('no hits')
#             return
#
#         print('hit', self.hits)1
#         # self.hits = [e.entity for e in self.hits]
#         # new_hits = []
#         # for hit in self.hits:
#         #     if matching_entities:
#         #         new_hits.append(matching_entities[0])
#         #
#         # self.
#         # matching_entities = [e for e in scene.entities if e.b == self.hits[0]]
#         # print(matching_entities)
#         # if matching_entities:
#         #     self.hovered_entity = matching_entities[0]
#         # else:
#         #     self.hovered_entity = None
#         # self.hits = [e for e in self.hits if e.collision]
#         # self.hits = [e.entity for e in self.hits if hasattr(e,'entity') and e.entity.collision]
#         # print(self.hits)
#         # return
#         #
#         # if self.hits:
#         #     self.hovered_entity = self.hits[0]
#
#         # print(self.hovered_entity)
#         # except:
#         #     self.hovered_entity = None
#         # ray = raycast(self.position)
#         # self.hovered_entity = ray.entity
#         # self.point = ray.point
#         # # print(self.point)
#         #
#         # if self.hovered_entity == None:
#         #     # unhover all if it didn't hit anything
#         #     for entity in scene.entities:
#         #         if entity.hovered:
#         #             entity.hovered = False
#         #             self.hovered_entity = None
#         #             if hasattr(entity, 'on_mouse_exit'):
#         #                 entity.on_mouse_exit()
#         #             for s in entity.scripts:
#         #                 if hasattr(s, 'on_mouse_exit'):
#         #                     s.on_mouse_exit()
# import time
# mouse = Mouse()


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
        # self.mouse_down_names = ('left mouse down', 'middle mouse down', 'right mouse down')
        # self.mouse_up_names = ('left mouse up', 'middle mouse up', 'right mouse up')
        #
        # def _mousedown(event):
        #     i = min(event.which-1, 3)
        #     self.input(self.mouse_down_names[i])
        # def _mouseup(event):
        #     i = min(event.which-1, 3)
        #     self.input(self.mouse_up_names[i])
        # def _mousescroll(event):
        #     self.input('scroll down' if event.deltaY > 0 else 'scoll up')
        # def _mousemove(event):
        #     mouse._mouse_event = event
        #     mouse.position = (
        #         min(max(
        #             (event.x-window.position[0]-(window.size[0]/2))/window.size[0]*window.aspect_ratio,
        #             -window.aspect_ratio/2,
        #             ), window.aspect_ratio/2),
        #         min(max(
        #             ((-event.y-window.position[1])/window.size[1]) +.5,
        #             -.5
        #             ), .5)
        #         )
        #
        # document.addEventListener('mousedown', _mousedown)
        # document.addEventListener("mouseup", _mouseup)
        # document.addEventListener("wheel", _mousescroll)
        # document.addEventListener("mousemove", _mousemove)



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
            # mouse.update()
            if hasattr(__main__, 'update'):
                __main__.update()
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
