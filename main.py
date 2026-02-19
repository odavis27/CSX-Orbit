from calc_position import *
from simulation_class import *

new_sim = simulation()

t = 0
p = planet(MH = 1.989e30, XP = 149999549.8, VyP = 5.81e5, MP = 5.97e24, XH = -450.224, VyH = 0)
# p.M = 1.989e30
# p.X = 1.5e8
# p.Vy = 581000
# p2.M = 5.97e24
# p2.X = 0
# p2.Vy = 0

planet_X = []
planet_Y = []
host_X = []
host_Y = []

def anim(i):
    global t, p
    pos = p.calc_pos()
    # planet_X.append(pos[0])
    # planet_Y.append(pos[1])
    # new_sim.draw(planet_X[-1], planet_Y[-1])
    # new_sim.trail(planet_X, planet_Y)
    host_X.append(pos[2])
    host_Y.append(pos[3])
    new_sim.draw(host_X[-1], host_Y[-1])
    new_sim.trail(host_X, host_Y)
    print(p.XH)
    t += p.T

fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), anim, interval=.5)
plt.show()
