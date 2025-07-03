# from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT
import numpy as np
import glfw
from OpenGL.GL import *
from groovepy.core.window import Window
from groovepy.utils.logger import get_logger
from groovepy.renderer.renderer import Shader

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
    # shaders
    shader = Shader(
        "groovepy/renderer/shaders/basic.vert",
        "groovepy/renderer/shaders/basic.frag"
    )

    # Triangle data (positions only)
    vertices = np.array([
         0.0,  0.5, 0.0,   # top
        -0.5, -0.5, 0.0,   # bottom left
         0.5, -0.5, 0.0    # bottom right
    ], dtype=np.float32)

    # Generate and bind Vertex Array Object (VAO)
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # Generate Vertex Buffer Object (VBO)
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # Set vertex attribute pointer
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * vertices.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Unbind
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    while not win.should_close():
        glClear(GL_COLOR_BUFFER_BIT)
        do_something(42)

        shader.use()

        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)  # draw 3 vertices as 1 triangle
        glBindVertexArray(0)

        if win.keyboard.is_pressed('W'):
            print("Move camera forward")
        if win.keyboard.is_pressed('ESC'):
            glfw.set_window_should_close(win._window, True)

        win.swap_buffers()
        win.poll_events()
    win.terminate()

if __name__ == "__main__":
    main()
