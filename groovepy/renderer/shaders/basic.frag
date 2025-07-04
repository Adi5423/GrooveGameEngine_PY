#version 330 core

in vec3 vColor;         // received from vertex shader
out vec4 FragColor;

void main()
{
    FragColor = vec4(vColor, 1.0);
}
