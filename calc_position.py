#from simulation_class import *

G = 6.67*(10**-11)

class planet:
    def __init__(self):
        self.T = 1
        self.M_host = 1.989e30
        self.X = 1.496e11
        self.Y = 0
        self.Vx = 0
        self.Vy = 581000
        self.ax = -1*G*self.M_host*self.X/(self.X**2+self.Y**2)**1.5
        self.ay = -1*G*self.M_host*self.Y/(self.X**2+self.Y**2)**1.5

def calc_pos(T, p):
    global G
    X = p.X+(p.Vx*T)
    Y = p.Y+(p.Vy*T)
    p.ax = -1*G*p.M_host*X/(X**2+Y**2)**1.5
    p.ay = -1*G*p.M_host*Y/(X**2+Y**2)**1.5
    p.Vx = p.Vx+p.ax*T
    p.Vy = p.Vy+p.ay*T
    return (X, Y)

