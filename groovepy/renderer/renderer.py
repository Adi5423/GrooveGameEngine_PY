# groovepy/renderer/renderer.py

import os
from OpenGL.GL import *
from groovepy.utils.logger import get_logger

log = get_logger(__name__)

class Shader:
    def __init__(self, vertex_path: str, fragment_path: str):
        self.vertex_src = self._load_source(vertex_path)
        self.fragment_src = self._load_source(fragment_path)
        self.id = self._create_program()

    def _load_source(self, filepath: str) -> str:
        if not os.path.isfile(filepath):
            log.error("Shader file not found: %s", filepath)
            raise FileNotFoundError(filepath)
        with open(filepath, 'r') as f:
            return f.read()

    def _compile_shader(self, source: str, shader_type: int) -> int:
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)

        # Check compile status
        status = glGetShaderiv(shader, GL_COMPILE_STATUS)
        if not status:
            msg = glGetShaderInfoLog(shader).decode()
            log.error("Shader compile error (%s): %s", shader_type, msg)
            glDeleteShader(shader)
            raise RuntimeError(msg)
        log.debug("Compiled shader %s successfully", shader_type)
        return shader

    def _create_program(self) -> int:
        vert = self._compile_shader(self.vertex_src, GL_VERTEX_SHADER)
        frag = self._compile_shader(self.fragment_src, GL_FRAGMENT_SHADER)

        program = glCreateProgram()
        glAttachShader(program, vert)
        glAttachShader(program, frag)
        glLinkProgram(program)

        # Check link status
        status = glGetProgramiv(program, GL_LINK_STATUS)
        if not status:
            msg = glGetProgramInfoLog(program).decode()
            log.error("Program link error: %s", msg)
            glDeleteProgram(program)
            raise RuntimeError(msg)

        # Cleanup shaders after linking
        glDeleteShader(vert)
        glDeleteShader(frag)
        log.info("Shader program linked (ID: %d)", program)
        return program

    def use(self):
        glUseProgram(self.id)

    def set_uniform1i(self, name: str, value: int):
        loc = glGetUniformLocation(self.id, name)
        glUniform1i(loc, value)

    # You can add more set_uniformX methods as needed...
