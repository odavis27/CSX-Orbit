from calc_position import *
from simulation_class import *

new_sim = simulation()


t = 0

# when in doubt go back here
one = planet(mass = 5.972e24, X = -9.700e8, Y=2.431e8, Vy=0.2729, Vx=294.3)
two = planet(mass = 5.972e24, X=9.700e8, Y=-2.431e8, Vy=0.2729, Vx=294.3)      # 5.972e24
three = planet(mass = 5.972e24, X=0, Vy=-0.5458, Vx=-588.6)


#earth = planet(mass = 1.989e24, X = -74960000, Vy=670000)

# one = planet(mass = 1.989e30, X = -1.451e11, Y=3.636e10, Vy=12874, Vx=13881)
# #earth = planet(mass = 1.989e24, X = -74960000, Vy=670000)
# two = planet(mass = 1.989e30, X=1.451e11, Y=3.636e10, Vy=-12874, Vx=13881)
# three = planet(mass = 1.989e30, X=0, Vy=-27762, Vx=-25748)
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
third_X = []
third_Y = []

celestial_bodies = (one,two,three)
def anim(i):
    global t
    onepos = one.calc_pos([two,three])
    planet_X.append(onepos[0])
    planet_Y.append(onepos[1])
    twopos = two.calc_pos([one,three])
    host_X.append(twopos[0])
    host_Y.append(twopos[1])
    threepos = three.calc_pos([one,two])
    #planet_X.append(threepos[0])
    #planet_Y.append(threepos[1])

    new_sim.draw(((one.X,one.Y,10,'red'),(two.X,two.Y,10,'green'),(three.X,three.Y,10,'blue')))
    #new_sim.draw([(planet_X[-1], planet_Y[-1], 8, "black")])
    #new_sim.draw([(sun.X,sun.Y,10,'green')])
    #new_sim.trail(planet_X, planet_Y,col="black")
    #new_sim.trail(host_X, host_Y,col="green")

    t += one.T
    print(one.X)
fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), anim, interval=.001)
plt.show()
