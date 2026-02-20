#from simulation_class import *
from math import sqrt

G = 6.67*(10**-11)

class planet:
    def __init__(self,mass,X=0,Y=0,Vx=0,Vy=0):
        self.T = 1
        self.mass = mass
        self.X = X
        self.Y = Y
        #self.ax = -1*G*self.M_host*self.X/((self.X**2+self.Y**2)**1.5)
        #self.ay = -1*G*self.M_host*self.Y/((self.X**2+self.Y**2)**1.5)
        self.ax = 0
        self.ay = 0
        self.Vx = Vx
        #self.Vy = 581000
        self.Vy = Vy

    def calc_pos(self,bodies):
        temp_aX = 0
        temp_aY = 0

        p = self
        global G
        p.X = p.X+(p.Vx*p.T)
        p.Y = p.Y+(p.Vy*p.T)
        for host in bodies:
            p.ax = -1*G*(host.mass)*(p.X-(host.X))/(((p.X-host.X)**2+(p.Y-host.Y)**2)**1.5)
            p.ay = -1*G*(host.mass)*(p.Y-host.Y)/(((p.X-host.X)**2+(p.Y-host.Y)**2)**1.5)
        
        distance = sqrt((self.X-host.X)**2+(self.Y-host.Y)**2)
        self.X_force = -(G*((host.mass*self.mass)/distance**2))*(self.X/distance)
        self.Y_force = -(G*((host.mass*self.mass)/distance**2))*(self.Y/distance)
        self.ax = (self.X_force)/self.mass
        self.ay = (self.Y_force)/self.mass
        p.Vx = p.Vx+p.ax*p.T
        p.Vy = p.Vy+p.ay*p.T
        return (p.X, p.Y)