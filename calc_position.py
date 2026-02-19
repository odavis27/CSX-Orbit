#from simulation_class import *

G = 6.67*(10**-11)

class planet:
    def __init__(self, M, X, Vy):
        self.T = .5
        self.M = M
        self.X = X
        self.Y = 0
        self.ax = -1*G*self.M*self.X/((self.X**2+self.Y**2)**1.5)
        self.ay = -1*G*self.M*self.Y/((self.X**2+self.Y**2)**1.5)
        self.Vx = 0
        self.Vy = Vy

    def calc_pos(self):
        global G
        self.X = self.X+(self.Vx*self.T)
        self.Y = self.Y+(self.Vy*self.T)
        self.ax = -1*G*self.M*self.X/((self.X**2+self.Y**2)**1.5)
        self.ay = -1*G*self.M*self.Y/((self.X**2+self.Y**2)**1.5)
        self.Vx = self.Vx+self.ax*self.T
        self.Vy = self.Vy+self.ay*self.T
        return (self.X, self.Y)
