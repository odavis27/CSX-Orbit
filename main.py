from calc_position import *
from simulation_class import *
from parameters import *

print("oogldeyboogldy\n\n\n\n\n\n\noogldeyboogldyoogldeyboogldyoogldeyboogldyoogldeyboogldy")
col = "blue"
new_sim = simulation(col)

t = 0
p = planet()
new_sim.add_ball(0, 0)
def anim(i):
    global t, p
    t += p.T
    new_sim.draw(with_trails=True)
    pos = calc_pos(t,p)
    print(pos)
    new_sim.add_ball(pos[0],pos[1])
    #new_sim.add_ball(x,100)

fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), anim, interval=100)
plt.show()