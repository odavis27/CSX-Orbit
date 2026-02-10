from calc_position import *
from simulation_class import *
from parameters import *
from math import sqrt

col = "black"
new_sim = simulation(col)

def short(x,p):
    return (x*(10**p))/(10**p)
def dist(p1,p2):
    #x1,y1,x2,y2
    sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
t = 0
p = planet()
new_sim.add_ball(0, 0)
prev_dist = None
prev_spot = (0,0)
def anim(i):
    global t, p, prev_spot, prev_dist
    #new_sim.draw(with_trails=True)
    new_sim.balls[-1].plot(4)
    new_sim.draw_last_trails()
    pos = p.calc_pos()
    #print(pos)
    #print(p.Vx)
    new_sim.add_ball(short(pos[0],3),short(pos[1],3))
    #new_sim.add_ball(x,100)
    # if t != 0:
    #     new_dist = dist(prev_spot,pos)
    #     if prev_dist != None:
    #         if new_dist > prev_dist:
    #             new_sim.clear_balls()
    #         pass
    #         print(new_dist, prev_dist)
    #         print("---")
    #     else:
    #         prev_dist = new_dist
    # prev_spot = pos
    t += p.T


fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), anim, interval=5)
plt.show()