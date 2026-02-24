from calc_position import *
from simulation_class import *

new_sim = simulation()


t = 0

# defining the celestial bodies
body_1 = planet(mass = 1.989e30, X = -44960000, Vy=670000)
body_2 = planet(mass = 1.989e30, X=44960000, Vy=-670000, Vx=1)

# low delta t because the orbits are relatively small
body_1.T = 0.3
body_2.T = 0.3

planet_X, planet_Y = [], []
host_X, host_Y = [], []

celestial_bodies = (body_1,body_2)
def anim(i):
    global t
    pos_planet = body_1.calc_pos([body_2])
    planet_X.append(pos_planet[0])
    planet_Y.append(pos_planet[1])
    body_2pos = body_2.calc_pos([body_1])
    host_X.append(body_2pos[0])
    host_Y.append(body_2pos[1])

    new_sim.draw(((planet_X[-1], planet_Y[-1], 8, "black"),(body_2.X,body_2.Y,10,'green')))
    #new_sim.draw([(planet_X[-1], planet_Y[-1], 8, "black")])
    #new_sim.draw([(body_2.X,body_2.Y,10,'green')])
    print(body_2pos)
    new_sim.trail(planet_X, planet_Y,col="black")
    new_sim.trail(host_X, host_Y,col="green")
    t += body_1.T

fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), anim, interval=.5)
plt.show()
