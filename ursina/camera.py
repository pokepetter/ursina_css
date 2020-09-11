from ursina.main import _window
from ursina.main import scene
from ursina.main import window
from ursina.entity import Entity


class Camera(Entity):
    def __init__(self):
        super().__init__()
        self.orthographic = True
        self.fov = 1
        self.ui = Entity(name='ui', z=-100, scale_x=1/self.aspect_ratio)
        _window.appendChild(self.ui.b)
        self.name = 'camera'


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

    @property
    def aspect_ratio(self):
        return window.aspect_ratio
# camera = Camera()
