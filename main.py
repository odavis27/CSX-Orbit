from calc_position import *
from simulation_class import *

new_sim = simulation()

t = 0
p = planet(M = 1.989e30, X = 1.5e8, Vy = 581000)
p2 = planet(M = 5.97e24, X = 0.1, Vy = 0)
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
    planet_X.append(pos[0])
    planet_Y.append(pos[1])
    new_sim.draw_planet(planet_X[-1], planet_Y[-1])
    new_sim.trail(planet_X, planet_Y)
    pos2 = p2.calc_pos()
    host_X.append(pos2[0])
    host_Y.append(pos2[1])
    new_sim.draw_host(host_X[-1], host_Y[-1])
    new_sim.trail(host_X, host_Y)
    print(p.X)
    t += p.T

fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), anim, interval=.5)
plt.show()
