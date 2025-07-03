from setuptools import setup, find_packages

setup(
    name="groovepy",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "glfw", "PyOpenGL", "PyOpenGL-accelerate", "numpy"
    ],
    entry_points={
        "console_scripts": [
            "groove-demo = examples.simple_window:main"
        ]
    }
)