from simulation_class import *

T = 30
G = 6.67*10^-11
M_host = 1.99*10^30
X = 1.5*10^8
Y = 0
Vx = 0
Vy = 5.81*10^5
ax = -1*G*M_host*X/(X^2+Y^2)^1.5
ay = -1*G*M_host*Y/(X^2+Y^2)^1.5

def calc_pos(T, M_host):
    X = X+(Vx*T)
    Y = Y+(Vy*T)
    Vx = Vx+ax*T
    Vy = Vy+ay*T
    ax = -1*G*M_host*X/(X^2+Y^2)^1.5
    ay = -1*G*M_host*Y/(X^2+Y^2)^1.5
    return X, Y
