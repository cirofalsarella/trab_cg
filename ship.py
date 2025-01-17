import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math
import matrix

class Ship:
    def __init__(self, offset, x_0, y_0):
        # Salva os dados iniciais
        self.offset = offset
        self.x_0 = x_0
        self.y_0 = y_0

        # Salva os vertices do obj em um array
        self.vertices = self.setVertices()

    def setVertices(self):
        ## Polígono de 5 lados + círculo no 'meio'
        step = 16
        radius = 0.05

        vertices = np.zeros(21, [("position", np.float32, 2)])
        vertices[0] = [ 0.1,-0.2]
        vertices[1] = [-0.1,-0.2]
        vertices[2] = [ 0.1, 0.2]
        vertices[3] = [-0.1, 0.2]
        vertices[4] = [ 0.0, 0.4]

        for i in range(step):
            angle = math.pi * (2 * i/step)
            x = math.cos(angle)*radius
            y = math.sin(angle)*radius + 1.5 * radius

            vertices[i+5] = [x,y]

        
        return vertices

    def drawShape(self, loc_color, program, dg, tx, ty):
        ## Tanto rotaciona como translada
        mat_transformation = matrix.getMatrix(1, dg, self.x_0 + tx, self.y_0 + ty)
        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transformation)

        # red body
        rValueBody = 227.0 / 255.0
        gValueBody = 23.0 / 255.0
        bValueBody = 70.0 / 255.0
        glUniform4f(loc_color, rValueBody, gValueBody, bValueBody, 1.0)  
        glDrawArrays(GL_TRIANGLE_STRIP, self.offset, 4)

         # green top
        rValueTop = 115.0 / 255.0
        gValueTop = 222.0 / 255.0
        bValueTop = 33.0 / 255.0
        glUniform4f(loc_color, rValueTop, gValueTop, bValueTop, 1.0)   
        glDrawArrays(GL_TRIANGLES, self.offset + 2, 3)

        # white window
        ValueWindow = 1
        glUniform4f(loc_color, ValueWindow, ValueWindow, ValueWindow, 1.0) 
        glDrawArrays(GL_TRIANGLE_FAN, self.offset + 5, 16)