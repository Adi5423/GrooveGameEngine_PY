# groovepy/core/window.py
import glfw
from OpenGL.GL import *
from groovepy.input.keyboard import Keyboard

class Window:
    def __init__(self, width: int =800, height: int =600, title: str ="GroovePy"):
        if not glfw.init():
            raise RuntimeError("Failed to initialize GLFW")
        # Configure context (OpenGL 3.3 Core)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self._window = glfw.create_window(width, height, title, None, None)
        if not self._window:
            glfw.terminate()
            raise RuntimeError("Failed to create GLFW window")

        glfw.make_context_current(self._window)
        self.keyboard = Keyboard(self._window)
        # Optional: set callbacks here (resize, input, etc.)

    def poll_events(self):
        glfw.poll_events()

    def swap_buffers(self):
        glfw.swap_buffers(self._window)

    def should_close(self) -> bool:
        return glfw.window_should_close(self._window)

    def terminate(self):
        glfw.terminate()
