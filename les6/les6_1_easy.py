# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

class Triangle:
    
    def __init__(self, top_A, top_B, top_C ):
        self.top_A = [None]
        self.top_B = [None]
        self.top_C = [None]
        self.a = a
        self.b = b
        self.c = c
        self.p = p
        self.p_2 = p_2
        self.s = s
        self.h = h
        
    def length_of_sides(self, top_A, top_B, top_C ):
        self.a = math.sqrt((self.top_B[1] - self.top_A[1])**2 + (self.top_B[0] - self.top_A[0])**2)
        self.b = math.sqrt((self.top_C[1] - self.top_B[1])**2 + (self.top_C[0] - self.top_B[0])**2)
        self.c = math.sqrt((self.top_A[1] - self.top_C[1])**2 + (self.top_A[0] - self.top_C[0])**2)

    def perim_triangle(self, a, b, c):
        self.p = self.a + self.b + self.c
    
    def area_triangle(self, a, b, c, p):
        self.p_2 = self.p / 2
        self.s = math.sqrt(self.p_2 * (self.p_2 - self.a) * (self.p_2 - self.b) * (self.p_2 - self.c))

    def height_triangle(self, a, s):
        self.h = 2 * self.s / self.a

    def output_calc(self, s, p, h):
        print('area:', self.s)
        print('perimeter:', self.p)
        print('height:', self.h)
        
        

    
        
