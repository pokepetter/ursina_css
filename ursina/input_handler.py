# from collections import defaultdict
from enum import Enum



class InputEvents(Enum):
    left_mouse_down = 'left mouse down'
    left_mouse_up = 'left mouse up'
    middle_mouse_down = 'middle mouse down'
    middle_mouse_up = 'middle mouse up'
    right_mouse_down = 'right mouse down'
    right_mouse_up = 'right mouse up'
    scroll_up = 'scroll up'
    scroll_down = 'scroll down'
    arrow_left = 'left arrow'
    arrow_left_up = 'left arrow up'
    arrow_up = 'up arrow'
    arrow_up_up = 'up arrow up'
    arrow_down = 'down arrow'
    arrow_down_up = 'down arrow up'
    arrow_right = 'right arrow'
    arrow_right_up = 'right arrow up'
    left_control = 'left control'
    right_control = 'right control'
    left_shift = 'left shift'
    right_shift = 'right shift'
    left_alt = 'left alt'
    right_alt = 'right alt'
    left_control_up = 'left control up'
    right_control_up = 'right control up'
    left_shift_up = 'left shift up'
    right_shift_up = 'right shift up'
    left_alt_up = 'left alt up'
    right_alt_up = 'right alt up'
    page_down = 'page down'
    page_down_up = 'page down up'
    page_up = 'page up'
    page_up_up = 'page up up'
    enter = 'enter'
    backspace = 'backspace'
    escape = 'enter'
    tab = 'tab'

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        # overriden __eq__ to allow for both str and InputEvent comparisons
        if isinstance(other, InputEvents):
            return self.value == other.value
        return self.value == other



# held_keys = defaultdict(lambda: 0)
held_keys = dict()
for char in [chr(i) for i in range(127)]:
    held_keys[char] = 0

rebinds = dict()


def bind(original_key, alternative_key):
    rebinds[original_key] = alternative_key
    rebinds[original_key + ' hold'] = alternative_key + ' hold'
    rebinds[original_key + ' up'] = alternative_key + ' up'


def unbind(key):
    if key in rebinds:
        del rebinds[key]
        del rebinds[key + ' hold']
        del rebinds[key + ' up']
    else:
        rebinds[key] = 'none'


def rebind(to_key, from_key):
    unbind(to_key)
    bind(to_key, from_key)


def input(key):
    if key.endswith('hold') or key == InputEvents.scroll_down or key == InputEvents.scroll_up:
        return

    key = key.replace('mouse down', 'mouse')

    if key.endswith('up'):
        held_keys[key[:-3]] = 0
    else:
        held_keys[key] = 1



if __name__ == '__main__':
    from ursina import *

    app = Ursina()
    input_handler.bind('s', 'arrow down')  # 's'-key will now be registered as 'arrow down'-key

    # input_handler.rebind('a', 'f')
    def input(key):
        print(key)
        if key == 'left mouse down':
            print('pressed left mouse button')

        if key == InputEvent.left_mouse_down:   # same as above, but with InputEvents enum.
            print('pressed left mouse button')


    app.run()
