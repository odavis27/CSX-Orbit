from calc_position import *
from simulation_class import *

new_sim = simulation()


t = 0

# when in doubt go back here
earth = planet(mass = 1.989e30, X = -44960000, Vy=670000)
#earth = planet(mass = 1.989e24, X = -74960000, Vy=670000)
sun = planet(mass = 1.989e30, X=44960000, Vy=-670000, Vx=1)
# sun = planet(mass = 1.989e30, X=0, Vy=1, Vx=1)

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

celestial_bodies = (earth,sun)
def anim(i):
    global t
    pos_planet = earth.calc_pos([sun])
    planet_X.append(pos_planet[0])
    planet_Y.append(pos_planet[1])
    sunpos = sun.calc_pos([earth])
    host_X.append(sunpos[0])
    host_Y.append(sunpos[1])

    new_sim.draw(((planet_X[-1], planet_Y[-1], 8, "black"),(sun.X,sun.Y,10,'green')))
    #new_sim.draw([(planet_X[-1], planet_Y[-1], 8, "black")])
    #new_sim.draw([(sun.X,sun.Y,10,'green')])
    print(sunpos)
    new_sim.trail(planet_X, planet_Y,col="black")
    new_sim.trail(host_X, host_Y,col="green")

    t += earth.T

fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), anim, interval=.5)
plt.show()
