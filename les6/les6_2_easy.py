# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt 

class isosceles_trapezoid:
    
    def __init__():
        self.top_A = [None]
        self.top_B = [None]
        self.top_C = [None]
        self.top_D = [None]
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.s = s
        self.p = p
        self.d1 = d1
        self.d1 = d2 
        
    def length_of_sides(self, top_A, top_B, top_C, top_D):
        self.c = math.sqrt((self.top_B[1] - self.top_A[1])**2 + (self.top_B[0] - self.top_A[0])**2)
        self.b = math.sqrt((self.top_C[1] - self.top_B[1])**2 + (self.top_C[0] - self.top_B[0])**2)
        self.d = math.sqrt((self.top_D[1] - self.top_C[1])**2 + (self.top_D[0] - self.top_C[0])**2)
        self.a = math.sqrt((self.top_A[1] - self.top_D[1])**2 + (self.top_A[0] - self.top_D[0])**2)

    def area_iso_trapez(self, a, b, c, d):
        self.s = (self.a + self.b) / 4 * math.sqrt(4 * (self.c**2) - (self.a - self.b)**2)

    def perim_iso_trapez(self, a, b, c, d):
        self.p = self.a + self.b + self.c + self.d

    def diags_of_trapez(self, a, b, c, d):
        self.d1 = sqrt(self.d**2 + self.a * self.b - (self.a * (self.d**2 - self.c**2)) / (self.a - self.b))
        self.d2 = sqrt(self.c**2 + self.a * self.b - (self.a * (self.c**2 - self.d**2)) / (self.a - self.b))

    def compar_diags(self, d1, d2):
        if self.d1 == self.d2:
            return 1
        else:
            return 0

    def output_calc(self, s, p, a, b, c, d):
        print('area:', self.s)
        print('perimiter:', self.p)
        print('length of bases:', 'a =', self.a, 'b =', self.b )
        print('length of sides:', 'c =', self.c, 'd =', self.d )
        





























        

            
    
