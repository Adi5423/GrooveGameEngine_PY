#version 330 core

layout (location = 0) in vec3 aPos;    // vertex position
layout (location = 1) in vec3 aColor;  // vertex color

out vec3 vColor;                       // pass to fragment

void main()
{
    vColor = aColor;                                 // forward the color
    gl_Position = vec4(aPos, 1.0);                   // set clip‑space position
}
