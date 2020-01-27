import pyglet
from pyglet import gl
def draw_rect(x, y, width, height,colour):
    gl.glColor3f(colour[0],colour[1],colour[2])
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ('v2f', [x, y, x + width, y, x + width, y + height, x, y + height]))
