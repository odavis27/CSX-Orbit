#from simulation_class import *
from math import sqrt

G = 6.67*(10**-11)

class planet:
    def __init__(self,mass,X=0,Y=0,Vx=0,Vy=0):
        self.T = 1
        self.mass = mass
        self.X = X
        self.Y = Y
        self.ax = 0
        self.ay = 0
        self.Vx = Vx
        self.Vy = Vy

    def calc_pos(self,bodies):
        total_ax = 0
        total_ay = 0
        p = self
        global G
        
        for host in bodies:
            dx = host.X - p.X
            dy = host.Y - p.Y
            distance = sqrt(dx**2 + dy**2)
            
            if distance < 1: continue 
            accel = (G * host.mass) / (distance**2)
            
            total_ax += accel * (dx / distance)
            total_ay += accel * (dy / distance)
        
        p.ax = total_ax
        p.ay = total_ay
        p.Vx = p.Vx + p.ax * p.T
        p.Vy = p.Vy + p.ay * p.T
        p.X = p.X + (p.Vx * p.T)
        p.Y = p.Y + (p.Vy * p.T)
        
        return (p.X, p.Y)