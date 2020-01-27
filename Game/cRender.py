import pyglet
from pyglet import gl
def draw_rect(x, y, width, height,colour):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ('v2f', [x, y, x + width, y, x + width, y + height, x, y + height]),
        ('c3B',colour*4))
