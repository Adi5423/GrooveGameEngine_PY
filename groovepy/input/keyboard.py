# groovepy/input/keyboard.py

import glfw
from groovepy.utils.logger import get_logger

log = get_logger(__name__)

# You can expand this dictionary to map more keys
_KEYS = {
    'W': glfw.KEY_W,
    'A': glfw.KEY_A,
    'S': glfw.KEY_S,
    'D': glfw.KEY_D,
    'ESC': glfw.KEY_ESCAPE,
}

class Keyboard:
    def __init__(self, window):
        self._window = window
        # A dict to hold press/release status
        self._key_states = {code: False for code in _KEYS.values()}
        # Register callback
        glfw.set_key_callback(window, self._on_key)

    def _on_key(self, window, key, scancode, action, mods):
        if key in self._key_states:
            pressed = action != glfw.RELEASE
            self._key_states[key] = pressed
            log.debug("Key %s: %s", key, "pressed" if pressed else "released")

    def is_pressed(self, key_name: str) -> bool:
        """Check if a named key is currently held down."""
        code = _KEYS.get(key_name.upper())
        if code is None:
            log.warning("Unknown key queried: %s", key_name)
            return False
        return self._key_states.get(code, False)
