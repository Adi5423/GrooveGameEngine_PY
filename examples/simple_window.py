# from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT
import numpy as np
import glfw
from OpenGL.GL import *
from groovepy.core.window import Window
from groovepy.utils.logger import get_logger
from groovepy.renderer.renderer import Shader
from groovepy.renderer.mesh import Mesh

# logger
log = get_logger(__name__)

# value = maybe deltatime 
def do_something(value):
    log.info("Starting operation")
    try:
        # ...
        log.debug("Intermediate value: %s", value)
    except Exception as e:
        log.error("Failed: %s", e)

def main():
    win = Window(640, 480, "GroovePy Demo")

    # 1) create shader _after_ context is current
    shader = Shader("groovepy/renderer/shaders/basic.vert",
                    "groovepy/renderer/shaders/basic.frag")

    # 2) prepare a Mesh with pos+color
    vertices = np.array([
        # positions        # colors
        -0.5, -0.5, 0.0,    1.0, 0.0, 0.0,  # bottom‑left red
         0.5, -0.5, 0.0,    0.0, 1.0, 0.0,  # bottom‑right green
         0.0,  0.5, 0.0,    0.0, 0.0, 1.0,  # top blue
    ], dtype=np.float32)
    mesh = Mesh(vertices)

    # 3) render loop
    while not win.should_close():
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        shader.use()
        mesh.draw()

        if win.keyboard.is_pressed('ESC'):
            glfw.set_window_should_close(win._window, True)

        win.swap_buffers()
        win.poll_events()

    win.terminate()

if __name__ == "__main__":
    main()
