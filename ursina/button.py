from ursina import *


class Button(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.collision = True
        self.text_entity = Text(parent=self, origin=(0,0))
        self.text = ''
        self.model = 'quad'
        self.color = color.black66
        self.highlight_color = color.hsv(0,0,.2,.8)
        self.collision = True
        self.name = 'button'

        for key, value in kwargs.items():
            setattr(self, key ,value)


    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name == 'text' and value:  self.text_entity.b.innerHTML = value

        if name == 'color':
            self._original_color = value

    @property
    def on_click(self):
        return self._on_click

    @on_click.setter
    def on_click(self, value):
        self._on_click = value
        self.b.onclick = self._click_callback

    def _click_callback(self, ev):
        if hasattr(self, '_on_click') and self.collision:
            self._on_click()


    def on_mouse_enter(self):
        self._original_color = self.color
        self.b.style.backgroundColor = self.highlight_color

    def on_mouse_exit(self):
        self.b.style.backgroundColor = self._original_color
