#from simulation_class import *

G = 6.67*(10**-11)

class planet:
    def __init__(self):
        self.T = 10
        self.M_host = 1.989e30
        self.X = 150000000
        self.Y = 0
        self.ax = -1*G*self.M_host*self.X/((self.X**2+self.Y**2)**1.5)
        self.ay = -1*G*self.M_host*self.Y/((self.X**2+self.Y**2)**1.5)
        self.Vx = 0
        self.Vy = 581000

    def calc_pos(self):
        p = self
        global G
        p.X = p.X+(p.Vx*p.T)
        p.Y = p.Y+(p.Vy*p.T)
        p.ax = -1*G*p.M_host*p.X/((p.X**2+p.Y**2)**1.5)
        p.ay = -1*G*p.M_host*p.Y/((p.X**2+p.Y**2)**1.5)
        p.Vx = p.Vx+p.ax*p.T
        p.Vy = p.Vy+p.ay*p.T
        return (p.X, p.Y)